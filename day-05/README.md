# 🎯 Number Guessing Game

A simple Python game where the computer picks a random number and the player tries to guess it.

## 🚀 How it works

- The computer selects a random number between 1 and 100
- The player tries to guess it
- The program gives hints:
  - 📈 "Go Higher" if the guess is too low
  - 📉 "Go Lower" if the guess is too high
- The game ends when the correct number is guessed

## 💻 Code

```python
import random

secret_number = random.randint(1, 100)
guess = int(input('Guess The Number: '))

while guess != secret_number:
    if guess < secret_number:
        print('Go Higher')
    else:
        print('Go Lower')

    guess = int(input('Guess Again: '))

print('You Are Right!')
```

## 🎮 Example

**Input:**
```text
Guess The Number: 50
Go Higher
Guess Again: 80
Go Lower
Guess Again: 65
You Are Right!
```

## 🧠 Concepts used

- Random numbers (`random.randint`)
- While loops
- Conditional statements (`if/else`)
- User input
- Basic game logic

## 🛠 Requirements

- Python 3.x

---

Made with Python 🐍