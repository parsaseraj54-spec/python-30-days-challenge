# Word Counter 📝

A simple Python program that counts the number of words in a sentence entered by the user.

---

## Features

- ✍️ Accepts a sentence from the user
- 🔢 Counts the number of words
- 📄 Displays the total word count

---

## How It Works

The program:

1. Gets a sentence from the user
2. Splits the sentence into words
3. Counts the words
4. Prints the result

---

## Example

Input:
Write a Sentence: Python is fun to learn

Output:
Word Numbers: 5

---

## Code Overview

```python
sentence = input('Write a Sentence: ')
words = sentence.split()

count = len(words)

print(f'Word Numbers: {count}')
```

---

## Concepts Practiced

- User input
- String methods
- `.split()`
- `len()`
- Variables

---

## Possible Improvements

- Count characters
- Count letters without spaces
- Count repeated words
- Ignore punctuation marks

---

## Author

Made with Python by **Parsa Seraj**