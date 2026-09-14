"""Integration tests for the original interactive password checker."""

import subprocess
import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CHECKER = PROJECT_ROOT / "src" / "password_strength_checker.py"


def run_checker(password: str) -> subprocess.CompletedProcess[str]:
    """Run the real interactive program with one password."""
    return subprocess.run(
        [sys.executable, str(CHECKER)],
        input=f"{password}\n",
        text=True,
        capture_output=True,
        cwd=PROJECT_ROOT,
        timeout=10,
        check=False,
    )


class PasswordStrengthCheckerIntegrationTests(unittest.TestCase):
    def test_very_strong_password_scores_five(self) -> None:
        completed = run_checker("Strong1!")
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIn("Author: MOOKTY", completed.stdout)
        self.assertIn("Version: 1.0", completed.stdout)
        self.assertIn("Password Very Strong", completed.stdout)

    def test_medium_password_scores_at_least_three(self) -> None:
        completed = run_checker("Password")
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIn("Password Medium Strength", completed.stdout)

    def test_weak_password_scores_below_three(self) -> None:
        completed = run_checker("abc")
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIn("Password Weak", completed.stdout)


if __name__ == "__main__":
    unittest.main()
