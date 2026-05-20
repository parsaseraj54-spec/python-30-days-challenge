# Password Strength Checker 🔐

A Python program that checks the strength of a password using different conditions and gives it a score.

---

## Features

- 📏 Checks password length
- 🔠 Detects uppercase letters
- 🔡 Detects lowercase letters
- 🔢 Detects numbers
- ✨ Detects special characters
- 📊 Calculates a password score

---

## How It Works

The program evaluates a password based on:

1. Length (8+ characters)
2. Uppercase letters
3. Lowercase letters
4. Numbers
5. Special characters

Each valid condition adds points and missing conditions reduce points.

---

## Example

Input:

Enter a Password: Parsa123!


Output:

5


---

## Code Overview

```python
password = input('Enter a Password: ')

score = 0

if len(password) >= 8:
    score += 1
else:
    score -= 1

has_upper = any(c.isupper() for c in password)

if has_upper:
    score += 1
else:
    score -= 1

has_lower = any(i.islower() for i in password)

if has_lower:
    score += 1
else:
    score -= 1

has_number = any(j.isdigit() for j in password)

if has_number:
    score += 1
else:
    score -= 1

has_others = any(not h.isalnum() for h in password)

if has_others:
    score += 1
else:
    score -= 1

print(score)
```

---

## Concepts Practiced

- User input
- Conditional statements
- Boolean values
- Loops inside functions
- `any()` function
- String methods
- Password validation logic

---

## Possible Improvements

- Display password strength levels:

  - Weak 🔴
  - Medium 🟡
  - Strong 🟢

- Show suggestions for improving weak passwords
- Prevent common passwords
- Hide password input while typing

---

## Author

Made with Python by **Parsa Seraj**