# >_ Password Strength Checker

A simple interactive Python tool that scores a password against five basic character-composition checks.

```text
mohammad@lab:~/password-strength-checker$ python src/password_strength_checker.py
============================================================
PASSWORD STRENGTH CHECKER
Author: MOOKTY
Version: 1.0
============================================================
Simple Password Strength Checker

Enter password to check: Strong1!
Password Very Strong
```

## Features

- Interactive password entry using `input()`
- Five-point strength score
- Checks minimum length, uppercase letters, lowercase letters, digits, and special characters
- Reports weak, medium, or very strong based on the final score
- Terminal banner generated with `pyfiglet`

## How the strength score works

The score starts at `0`. Each matching rule adds one point:

| Check | Point condition |
|---|---|
| Length | At least 8 characters |
| Uppercase | Contains `[A-Z]` |
| Lowercase | Contains `[a-z]` |
| Digit | Contains a decimal digit |
| Special character | Contains one character from the script's defined special-character set |

The final result is:

- `5`: Password Very Strong
- `3–4`: Password Medium Strength
- `0–2`: Password Weak

## Requirements

- Python 3.10 or newer
- `pyfiglet==1.0.4`

## Installation

```bash
git clone https://github.com/MOOKTY/password-strength-checker.git
cd password-strength-checker
python -m venv .venv
```

Activate the virtual environment:

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

```bash
# Linux or macOS
source .venv/bin/activate
```

Install the dependency:

```bash
python -m pip install -r requirements.txt
```

## Usage

```bash
python src/password_strength_checker.py
```

Enter a password when prompted. The program prints its classification after applying the five checks.

## Example output

```text
Enter password to check: Strong1!
Password Very Strong
```

## Technologies used

- Python
- Standard-library `re` module
- `pyfiglet` for the terminal banner
- `unittest` and `subprocess` for integration testing

## Project structure

```text
password-strength-checker/
├── src/
│   └── password_strength_checker.py
├── tests/
│   └── test_password_strength_checker.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Limitations

- The score uses only five basic composition checks.
- It does not calculate entropy or estimate cracking time.
- It does not check breached-password databases or external APIs.
- Password input is visible while it is typed because the program uses `input()`.
- A high score is not a guarantee that a password is secure.

## Privacy note

The current tool evaluates the entered password locally. It does not intentionally save, log, or transmit the password. Because it uses standard `input()`, the password remains visible in the terminal while it is typed.

## Future improvements

Potential improvements can be considered in later versions. This repository documents version 1.0 and does not claim features that are absent from the original implementation.

## License

Released under the [MIT License](LICENSE).

## Author

Mohammad Okasha  
GitHub: [@MOOKTY](https://github.com/MOOKTY)
