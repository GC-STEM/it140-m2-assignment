"""Check README Bash command blocks for cross-platform shell compatibility."""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
README_NAMES = {"README.md", "RЕADME.md"}
MARKER_RE = re.compile(r"<!--\s*ci:command-test\s+(.+?)\s*-->")
ATTRIBUTE_RE = re.compile(r"([a-z][a-z0-9_-]*)=([A-Za-z0-9_-]+)")
WINDOWS_DRIVE_RE = re.compile(r"(?<![A-Za-z0-9_])[A-Za-z]:[\\/]")
WINDOWS_HOME_BACKSLASH_RE = re.compile(r"(?:~|\$HOME)\\")

ALLOWED_FIXTURES = {"empty-repos", "existing-repo"}
ALLOWED_EXPECTATIONS = {"repos", "repo", "part-a"}


@dataclass(frozen=True)
class CommandBlock:
    """One Bash fenced code block from a README file."""

    path: Path
    line: int
    body: str
    test_id: str | None = None
    fixture: str | None = None
    expect: str | None = None

    @property
    def label(self) -> str:
        """Return a concise location for reports."""
        relative = self.path.relative_to(REPO_ROOT)
        if self.test_id:
            return f"{relative}:{self.line} ({self.test_id})"
        return f"{relative}:{self.line}"


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--shell",
        required=True,
        choices=("bash", "zsh"),
        help="Shell used to validate and run Bash documentation blocks.",
    )
    parser.add_argument(
        "--platform",
        required=True,
        choices=("linux", "macos", "windows-git-bash"),
        help="Platform label used in CI output.",
    )
    return parser.parse_args()


def readme_files() -> list[Path]:
    """Return README-style Markdown files in stable path order."""
    files = [
        path
        for path in REPO_ROOT.rglob("*.md")
        if path.name in README_NAMES
    ]
    return sorted(files, key=lambda path: path.as_posix())


def marker_attributes(line: str) -> dict[str, str] | None:
    """Parse a smoke-test marker from one Markdown line."""
    match = MARKER_RE.fullmatch(line.strip())
    if match is None:
        return None

    attributes = dict(ATTRIBUTE_RE.findall(match.group(1)))
    required = {"id", "fixture", "expect"}
    if set(attributes) != required:
        expected = "id=... fixture=... expect=..."
        raise ValueError(
            f"Command-test marker must contain exactly: {expected}"
        )
    if attributes["fixture"] not in ALLOWED_FIXTURES:
        raise ValueError(
            "Unknown fixture in command-test marker: "
            f"{attributes['fixture']}"
        )
    if attributes["expect"] not in ALLOWED_EXPECTATIONS:
        raise ValueError(
            "Unknown expected working directory in command-test marker: "
            f"{attributes['expect']}"
        )
    return attributes


def extract_bash_blocks(path: Path) -> list[CommandBlock]:
    """Extract Bash fences and optional smoke-test metadata."""
    lines = path.read_text(encoding="utf-8").splitlines()
    blocks: list[CommandBlock] = []
    pending: dict[str, str] | None = None
    pending_line = 0
    index = 0

    while index < len(lines):
        stripped = lines[index].strip()

        try:
            marker = marker_attributes(stripped)
        except ValueError as exc:
            relative = path.relative_to(REPO_ROOT)
            raise ValueError(f"{relative}:{index + 1}: {exc}") from exc

        if marker is not None:
            if pending is not None:
                relative = path.relative_to(REPO_ROOT)
                raise ValueError(
                    f"{relative}:{pending_line}: command-test marker is not "
                    "followed by a Bash code block."
                )
            pending = marker
            pending_line = index + 1
            index += 1
            continue

        if stripped.startswith("```"):
            info = stripped[3:].strip().lower()
            language = info.split(maxsplit=1)[0] if info else ""
            start_line = index + 1
            index += 1
            body_lines: list[str] = []
            while index < len(lines) and not lines[index].strip().startswith(
                "```"
            ):
                body_lines.append(lines[index])
                index += 1

            if index >= len(lines):
                relative = path.relative_to(REPO_ROOT)
                raise ValueError(
                    f"{relative}:{start_line}: unclosed fenced code block."
                )

            if language in {"bash", "sh", "shell"}:
                attributes = pending or {}
                blocks.append(
                    CommandBlock(
                        path=path,
                        line=start_line,
                        body="\n".join(body_lines) + "\n",
                        test_id=attributes.get("id"),
                        fixture=attributes.get("fixture"),
                        expect=attributes.get("expect"),
                    )
                )
                pending = None
                pending_line = 0
            elif pending is not None:
                relative = path.relative_to(REPO_ROOT)
                raise ValueError(
                    f"{relative}:{pending_line}: command-test marker must be "
                    "followed by a Bash code block."
                )

            index += 1
            continue

        if pending is not None and stripped:
            relative = path.relative_to(REPO_ROOT)
            raise ValueError(
                f"{relative}:{pending_line}: command-test marker must be "
                "immediately followed by a Bash code block."
            )

        index += 1

    if pending is not None:
        relative = path.relative_to(REPO_ROOT)
        raise ValueError(
            f"{relative}:{pending_line}: command-test marker has no Bash "
            "code block."
        )

    return blocks


def policy_errors(block: CommandBlock) -> list[str]:
    """Return cross-platform documentation policy violations."""
    errors: list[str] = []
    text = block.body

    if "%USERPROFILE%" in text.upper():
        errors.append("uses cmd.exe %USERPROFILE% syntax in a Bash block")
    if "$env:" in text.lower():
        errors.append("uses PowerShell $env: syntax in a Bash block")
    if WINDOWS_DRIVE_RE.search(text):
        errors.append("uses a Windows drive path in a cross-platform Bash block")
    if WINDOWS_HOME_BACKSLASH_RE.search(text):
        errors.append("uses backslashes with ~ or $HOME in a Bash block")
    direct_code_path = re.search(
        r'(?im)^\s*code\s+["\']?(?:~|\$HOME)/Repos/',
        text,
    )
    if direct_code_path:
        errors.append(
            "opens a ~/Repos path directly with code; use cd ... then code ."
        )
    return errors


def shell_check(shell: str, block: CommandBlock) -> str | None:
    """Return shell syntax error text, or None when syntax is valid."""
    result = subprocess.run(
        [shell, "-n"],
        input=block.body,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode == 0:
        return None
    return (result.stderr or result.stdout).strip() or "shell syntax error"


def fixture_home(root: Path, fixture: str) -> Path:
    """Create a disposable HOME directory for one smoke test."""
    home = root / "home"
    repos = home / "Repos"
    repos.mkdir(parents=True)

    if fixture == "existing-repo":
        assignment = repos / "it140-m2-assignment"
        (assignment / "Part-A" / "tests").mkdir(parents=True)
        (assignment / "Part-A" / "tests" / "test_name_age.py").write_text(
            "# CI fixture for README command smoke tests.\n",
            encoding="utf-8",
        )
        (assignment / "Part-A" / "src").mkdir(parents=True)

    return home


def shell_prelude() -> str:
    """Return harmless command shims used by marked smoke tests."""
    return r'''
set -e

code() {
    printf 'code|%s|%s\n' "$PWD" "$*" >> "$CI_COMMAND_LOG"
    if [ "$#" -ne 1 ] || [ "$1" != "." ]; then
        printf 'code shim expected exactly: code .\n' >&2
        return 64
    fi
}

git() {
    printf 'git|%s|%s\n' "$PWD" "$*" >> "$CI_COMMAND_LOG"
    return 0
}

gh() {
    printf 'gh|%s|%s\n' "$PWD" "$*" >> "$CI_COMMAND_LOG"

    if [ "${1:-}" = "api" ] && [ "${2:-}" = "user" ]; then
        printf 'ci-student\n'
        return 0
    fi

    if [ "${1:-}" = "repo" ] && [ "${2:-}" = "create" ]; then
        repo_name="${3:-}"
        if [ -z "$repo_name" ]; then
            printf '%s\n' 'gh repo create shim needs a repository name.' >&2
            return 65
        fi
        mkdir -p "$PWD/$repo_name"
        return 0
    fi

    if [ "${1:-}" = "repo" ] && [ "${2:-}" = "clone" ]; then
        source_repo="${3:-}"
        destination="${4:-${source_repo##*/}}"
        if [ -z "$destination" ]; then
            printf 'gh repo clone shim could not determine a destination.\n' >&2
            return 65
        fi
        mkdir -p "$PWD/$destination"
        return 0
    fi

    return 0
}

python3() {
    printf 'python3|%s|%s\n' "$PWD" "$*" >> "$CI_COMMAND_LOG"
    if [ "$#" -gt 0 ] && [ "${1#-}" = "$1" ] && [ ! -f "$1" ]; then
        printf 'python3 shim could not find documented file: %s\n' "$1" >&2
        return 66
    fi
    return 0
}
'''.lstrip()


def shell_epilogue() -> str:
    """Return working-directory assertions for a smoke test."""
    return r'''
case "$CI_EXPECT" in
    repos)
        ci_expected_path="$HOME/Repos"
        ;;
    repo)
        ci_expected_path="$HOME/Repos/it140-m2-assignment"
        ;;
    part-a)
        ci_expected_path="$HOME/Repos/it140-m2-assignment/Part-A"
        ;;
    *)
        printf 'Unknown CI_EXPECT value: %s\n' "$CI_EXPECT" >&2
        exit 67
        ;;
esac

if [ ! -d "$ci_expected_path" ]; then
    printf 'Expected directory was not created: %s\n' "$ci_expected_path" >&2
    exit 68
fi

ci_expected_cwd="$(cd "$ci_expected_path" && pwd -P)"
ci_actual_cwd="$(pwd -P)"
if [ "$ci_actual_cwd" != "$ci_expected_cwd" ]; then
    printf 'Unexpected final working directory.\n' >&2
    printf 'Expected: %s\n' "$ci_expected_cwd" >&2
    printf 'Actual:   %s\n' "$ci_actual_cwd" >&2
    exit 69
fi
'''.lstrip()


def run_smoke_test(shell: str, block: CommandBlock) -> str | None:
    """Run one marked block in a disposable environment with command shims."""
    assert block.fixture is not None
    assert block.expect is not None

    with tempfile.TemporaryDirectory(prefix="it140-readme-") as temp_dir:
        root = Path(temp_dir)
        home = fixture_home(root, block.fixture)
        log_path = root / "commands.log"

        environment = os.environ.copy()
        # Forward-slash paths work in Bash/zsh and avoid backslash parsing in
        # Git Bash when Python is running on a Windows hosted runner.
        environment["HOME"] = home.as_posix()
        environment["CI_COMMAND_LOG"] = log_path.as_posix()
        environment["CI_EXPECT"] = block.expect

        script = shell_prelude() + "\n" + block.body + "\n" + shell_epilogue()
        result = subprocess.run(
            [shell, "-e"],
            input=script,
            text=True,
            capture_output=True,
            env=environment,
            check=False,
        )

        if result.returncode == 0:
            return None

        details = (result.stderr or result.stdout).strip()
        if log_path.exists():
            log = log_path.read_text(encoding="utf-8").strip()
            if log:
                details = f"{details}\nCommand log:\n{log}".strip()
        return details or f"smoke test exited with {result.returncode}"


def main() -> None:
    """Check all README Bash blocks and run marked smoke tests."""
    args = parse_args()
    errors: list[str] = []
    blocks: list[CommandBlock] = []

    files = readme_files()
    if not files:
        errors.append("No README files were found.")

    for path in files:
        try:
            blocks.extend(extract_bash_blocks(path))
        except ValueError as exc:
            errors.append(str(exc))

    ids: set[str] = set()
    marked = 0

    for block in blocks:
        for violation in policy_errors(block):
            errors.append(f"{block.label}: {violation}.")

        syntax_error = shell_check(args.shell, block)
        if syntax_error:
            errors.append(
                f"{block.label}: {args.shell} syntax check failed:\n"
                f"{syntax_error}"
            )

        if block.test_id is None:
            continue

        marked += 1
        if block.test_id in ids:
            errors.append(f"Duplicate command-test id: {block.test_id}")
            continue
        ids.add(block.test_id)

        smoke_error = run_smoke_test(args.shell, block)
        if smoke_error:
            errors.append(
                f"{block.label}: smoke test failed on {args.platform} "
                f"with {args.shell}:\n{smoke_error}"
            )
        else:
            print(
                f"PASS: {block.label} on {args.platform} ({args.shell})."
            )

    if marked == 0:
        errors.append("No README Bash blocks are marked for smoke testing.")

    if errors:
        print("README command checks failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        raise SystemExit(1)

    print(
        f"PASS: Checked {len(blocks)} Bash block(s) in {len(files)} README "
        f"file(s); smoke-tested {marked} marked block(s) on "
        f"{args.platform} ({args.shell})."
    )


if __name__ == "__main__":
    main()
