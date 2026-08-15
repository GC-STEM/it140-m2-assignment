"""Acceptance tests for the Module Two name_age program.

Run this test file from the repository root using the VS Code integrated
terminal. Normally, this is ~/Repos/it140-m2-assignment. If you used a
different location, change the path accordingly in the commands below.

Open the integrated terminal in VS Code:
    Terminal > New Terminal

Codio Virtual Desktop (CVD) / macOS / Linux / Git Bash:
    cd ~/Repos/it140-m2-assignment
    python3 tests/test_name_age.py

Windows PowerShell (not the Command Prompt):
    cd ~/Repos/it140-m2-assignment
    py tests/test_name_age.py
"""

# === Imports ===
from datetime import date
from pathlib import Path
import subprocess
import sys
import unittest


# === Constants ===
PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROGRAM_PATH = PROJECT_ROOT / "src" / "name_age.py"


# === Classes ===
class NameAgeAcceptanceTests(unittest.TestCase):
    """Test name_age.py against the acceptance cases in the SRS."""

    def check_case(self, name: str, age: int) -> None:
        """Run and check one shared acceptance test case."""
        current_year = date.today().year
        expected_birth_year = current_year - age
        expected_result = (
            f"Hello {name}! You were born in {expected_birth_year}."
        )

        result = run_program(name, age)

        self.assertEqual(
            result.returncode,
            0,
            msg=f"Program ended with an error:\n{result.stderr}",
        )
        self.assertIn("What is your name? ", result.stdout)
        self.assertIn("How old are you? ", result.stdout)
        self.assertIn(expected_result, result.stdout)

    def test_1_typical_adult_age(self) -> None:
        """Test a typical adult age."""
        self.check_case("Jordan", 25)

    def test_2_different_adult_name_and_age(self) -> None:
        """Test different adult input values."""
        self.check_case("Casey", 42)

    def test_3_zero_age_edge_case(self) -> None:
        """Test zero as an age edge case."""
        self.check_case("Morgan", 0)

    def test_4_negative_age_edge_case(self) -> None:
        """Test a negative age without requiring validation."""
        self.check_case("Riley", -5)

    def test_5_age_over_100_edge_case(self) -> None:
        """Test an age greater than 100."""
        self.check_case("Taylor", 105)


# === Helper Functions ===
def run_program(
    name: str,
    age: int,
) -> subprocess.CompletedProcess[str]:
    """Run name_age.py with simulated user input."""
    test_input = f"{name}\n{age}\n"

    return subprocess.run(
        [sys.executable, str(PROGRAM_PATH)],
        input=test_input,
        text=True,
        capture_output=True,
        check=False,
    )


# === Main Guard ===
if __name__ == "__main__":
    unittest.main(verbosity=2)
