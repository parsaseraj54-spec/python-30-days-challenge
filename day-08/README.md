# Simple Calculator 🧮

A basic Python calculator that performs simple arithmetic operations between two numbers.

---

## Features

- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division
- 🚫 Handles invalid operations

---

## How It Works

The program:

1. Takes two numbers from the user
2. Asks for an operation (`+`, `-`, `*`, `/`)
3. Performs the calculation
4. Prints the result

---

## Example

Input:
Enter First number: 10  
Enter Second number: 5  
Choose Operation (+,-,*,/): *

Output:
50

---

## Code Overview

```python
number1 = float(input('Enter First number: '))
number2 = float(input('Enter Second number: '))

operation = input('Choose Operation (+,-,*,/): ')

if operation == '+':
    print(number1 + number2)
elif operation == '-':
    print(number1 - number2)
elif operation == '*':
    print(number1 * number2)
elif operation == '/':
    print(number1 / number2)
else:
    print('Invalid Operation')
```

---

## Concepts Practiced

- User input
- Conditional statements (`if/elif/else`)
- Basic math operations
- Working with floats
- Input validation (basic)

---

## Possible Improvements

- Handle division by zero
- Loop the calculator so it doesn’t exit after one calculation
- Add more operations (power, modulus)
- Improve UI (menu system)

---

## Author

Python beginner project by **Parsa**