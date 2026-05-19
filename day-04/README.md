# 🧮 Factorial Calculator (n!)

A simple Python program that calculates the **factorial of a number (n!)** using a loop.

## 🚀 What is factorial?

Factorial of a number `n` is:

```
n! = 1 × 2 × 3 × ... × n
```

Example:
```
5! = 1 × 2 × 3 × 4 × 5 = 120
```

## 💻 How it works

- Takes a number from the user
- Multiplies all numbers from 1 to n
- Prints the final result

## 📌 Code

```python
n = int(input('Enter a Number'))

result = 1
for i in range(1, n + 1):
    result = result * i

print(result)
```

## ▶️ Example

**Input:**
```text
Enter a Number: 5
```

**Output:**
```text
120
```

## 🧠 Concepts used

- Variables
- User input
- For loops
- `range()` function
- Multiplication logic

## 🛠 Requirements

- Python 3.x

---

Made with Python 🐍