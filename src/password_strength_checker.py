import re

from pyfiglet import Figlet


f = Figlet(font="Graffiti")

print("=" * 60)
print(f.renderText("Password Strength Checker"))
print("Author: MOOKTY")
print("Version: 1.0")
print("=" * 60)
print("Simple Password Strength Checker")
print()

password = input("Enter password to check: ")
strong = 0

if len(password) >= 8:
    strong += 1
if re.search(r"[A-Z]", password):
    strong += 1
if re.search(r"[a-z]", password):
    strong += 1
if re.search(r"\d", password):
    strong += 1
if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
    strong += 1

if strong == 5:
    print("Password Very Strong")
elif strong >= 3:
    print("Password Medium Strength")
else:
    print("Password Weak")
