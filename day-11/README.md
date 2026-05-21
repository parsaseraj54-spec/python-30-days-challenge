# Best Student Finder 🎓

A simple Python program that finds the student with the highest grade from a dictionary.

---

## Features

- 📚 Stores student names and grades
- 🔍 Compares all grades
- 🏆 Finds the best student
- 📊 Displays the highest grade

---

## How It Works

The program:

1. Stores student names and grades in a dictionary
2. Goes through each student and grade
3. Compares grades
4. Saves the highest score
5. Prints the best student and grade

---

## Example

Input Data:

```python
grades = {
    'Jack': 96,
    'Sam': 58,
    'Ema': 78,
    'Ana': 99
}
```

Output:

```text
Best Student Ana
Best Grade 99
```

---

## Code Overview

```python
grades = {
    'Jack': 96,
    'Sam': 58,
    'Ema': 78,
    'Ana': 99
}

best_student = ''
best_grade = 0

for student, grade in grades.items():
    if grade > best_grade:
        best_grade = grade
        best_student = student

print('Best Student', best_student)
print('Best Grade', best_grade)
```

---

## Concepts Practiced

- Dictionaries
- Variables
- `for` loops
- `.items()`
- Conditional statements
- Comparing values

---

## Possible Improvements

- Calculate average grade
- Find the lowest grade
- Display all students sorted by grades
- Allow user input for student data

---

## Author

Made with Python by **Parsa Seraj**