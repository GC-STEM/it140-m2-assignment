"""Validate the intentional starter state of the Module Two assignment."""

from __future__ import annotations

import ast
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
SOURCE_PATH = REPO_ROOT / "Part-A/src/name_age.py"
TEST_PATH = REPO_ROOT / "Part-A/tests/test_name_age.py"
REFLECTION_PATH = REPO_ROOT / "Part-B/ide_features.md"

EXPECTED_TEST_CASES = {
    "test_1_typical_adult_age": ("Jordan", 25),
    "test_2_different_adult_name_and_age": ("Casey", 42),
    "test_3_zero_age_edge_case": ("Morgan", 0),
    "test_4_negative_age_edge_case": ("Riley", -5),
    "test_5_age_over_100_edge_case": ("Taylor", 105),
}

SOURCE_TODO_MARKERS = (
    "TODO: Replace with a one-line summary",
    "TODO: Replace with a major input",
    "TODO: Replace with a major processing step",
    "TODO: Replace with a major output",
    "TODO: Replace with code to get user's name",
    "TODO: Replace with code to get user's age",
    "TODO: Replace with code to process data",
    "TODO: Replace with code to output formatted results",
)

REFLECTION_MARKERS = (
    "Your introduction text here.",
    "## Feature 1 – Name of Feature1",
    "Your feature 1 text here.",
    "## Feature 2 – Name of Feature2",
    "Your feature 2 text here.",
    "## Feature 3 – Name of Feature3",
    "Your feature 3 text here.",
    "Your conclusion text here.",
)


class StarterChecks:
    """Collect starter validation failures."""

    def __init__(self) -> None:
        self.errors: list[str] = []

    def error(self, message: str) -> None:
        """Record a failing starter check."""
        self.errors.append(message)

    def finish(self) -> None:
        """Print results and exit nonzero when starter checks fail."""
        if not self.errors:
            print("PASS: Course starter structure is intentionally incomplete.")
            print("PASS: Acceptance test definitions are intact.")
            print("PASS: Part B reflection starter text is intact.")
            return

        print("Course starter checks failed:", file=sys.stderr)
        for error in self.errors:
            print(f"- {error}", file=sys.stderr)
        raise SystemExit(1)


def is_docstring_statement(node: ast.stmt) -> bool:
    """Return True if a statement is a string-expression docstring."""
    return (
        isinstance(node, ast.Expr)
        and isinstance(node.value, ast.Constant)
        and isinstance(node.value.value, str)
    )


def check_source(checks: StarterChecks) -> None:
    """Verify name_age.py remains a valid, intentionally incomplete starter."""
    text = SOURCE_PATH.read_text(encoding="utf-8")
    try:
        tree = ast.parse(text, filename=str(SOURCE_PATH))
    except SyntaxError as exc:
        checks.error(f"Starter source is not valid Python: {exc}")
        return

    for marker in SOURCE_TODO_MARKERS:
        if marker not in text:
            checks.error(f"Starter source is missing marker: {marker!r}")

    imported_date = any(
        isinstance(node, ast.ImportFrom)
        and node.module == "datetime"
        and any(alias.name == "date" for alias in node.names)
        for node in tree.body
    )
    if not imported_date:
        checks.error("Starter must import date from datetime.")

    year_assignments = [
        node
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "CURRENT_YEAR"
            for target in node.targets
        )
    ]
    if len(year_assignments) != 1:
        checks.error("Starter must define CURRENT_YEAR exactly once.")
    else:
        expression = ast.unparse(year_assignments[0].value)
        if expression != "date.today().year":
            checks.error(
                "CURRENT_YEAR must remain assigned to date.today().year."
            )

    main_functions = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == "main"
    ]
    if len(main_functions) != 1:
        checks.error("Starter must contain exactly one main() function.")
    else:
        body = main_functions[0].body
        if len(body) != 1 or not is_docstring_statement(body[0]):
            checks.error(
                "Course starter main() must remain intentionally incomplete; "
                "only its docstring should be executable before students work."
            )

    guards = [
        node
        for node in tree.body
        if isinstance(node, ast.If)
        and "__name__" in ast.unparse(node.test)
        and "__main__" in ast.unparse(node.test)
    ]
    if len(guards) != 1:
        checks.error("Starter must contain one __main__ guard.")
    else:
        guard_calls_main = any(
            isinstance(node, ast.Expr)
            and isinstance(node.value, ast.Call)
            and isinstance(node.value.func, ast.Name)
            and node.value.func.id == "main"
            for node in guards[0].body
        )
        if not guard_calls_main:
            checks.error("The __main__ guard must call main().")


def check_tests(checks: StarterChecks) -> None:
    """Verify the supplied acceptance test suite still defines five tests."""
    text = TEST_PATH.read_text(encoding="utf-8")
    try:
        tree = ast.parse(text, filename=str(TEST_PATH))
    except SyntaxError as exc:
        checks.error(f"Acceptance test file is not valid Python: {exc}")
        return

    test_class = next(
        (
            node
            for node in tree.body
            if isinstance(node, ast.ClassDef)
            and node.name == "NameAgeAcceptanceTests"
        ),
        None,
    )
    if test_class is None:
        checks.error("Acceptance test class NameAgeAcceptanceTests is missing.")
        return

    test_functions = {
        node.name: node
        for node in test_class.body
        if isinstance(node, ast.FunctionDef)
        and node.name.startswith("test_")
    }
    actual_tests = set(test_functions)
    expected_tests = set(EXPECTED_TEST_CASES)
    if actual_tests != expected_tests:
        missing = sorted(expected_tests - actual_tests)
        extra = sorted(actual_tests - expected_tests)
        if missing:
            checks.error(f"Acceptance tests are missing: {', '.join(missing)}")
        if extra:
            names = ", ".join(extra)
            checks.error(f"Unexpected acceptance tests found: {names}")

    for test_name, expected_case in EXPECTED_TEST_CASES.items():
        function = test_functions.get(test_name)
        if function is None:
            continue
        expected_name, expected_age = expected_case
        found = False
        for node in ast.walk(function):
            if not isinstance(node, ast.Call):
                continue
            if not isinstance(node.func, ast.Attribute):
                continue
            if node.func.attr != "check_case" or len(node.args) != 2:
                continue
            name_arg, age_arg = node.args
            try:
                name_value = ast.literal_eval(name_arg)
                age_value = ast.literal_eval(age_arg)
            except (ValueError, TypeError):
                continue
            if (name_value, age_value) == (expected_name, expected_age):
                found = True
                break
        if not found:
            checks.error(
                f"Acceptance case changed in {test_name}; expected "
                f"{expected_name!r}, {expected_age}."
            )

    expected_path = 'PROJECT_ROOT / "src" / "name_age.py"'
    if expected_path not in text:
        checks.error("Acceptance tests no longer target src/name_age.py.")


def check_reflection(checks: StarterChecks) -> None:
    """Verify Part B still ships with its intended starter text."""
    text = REFLECTION_PATH.read_text(encoding="utf-8")
    for marker in REFLECTION_MARKERS:
        if marker not in text:
            checks.error(f"Part B starter is missing marker: {marker!r}")


def main() -> None:
    """Run all course-starter checks."""
    checks = StarterChecks()
    check_source(checks)
    check_tests(checks)
    check_reflection(checks)
    checks.finish()


if __name__ == "__main__":
    main()
