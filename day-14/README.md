# Notes Saver App 📝

A simple Python program that lets users write notes and save them into a text file.

---

## Features

- ✍️ Accepts user notes
- 💾 Saves notes into a text file
- 📂 Automatically creates the file if it doesn't exist
- ➕ Adds new notes without deleting previous ones

---

## How It Works

The program:

1. Asks the user to write a note
2. Opens `notes.txt` in append mode
3. Saves the note into the file
4. Adds a new line after each note
5. Displays a confirmation message

---

## Project Structure

```text
project-folder/
│
├── main.py
└── notes.txt
```

---

## Example

Input:

```text
Write a Note: Learn Python functions today
```

Output:

```text
Note saved.
```

Content inside `notes.txt`:

```text
Learn Python functions today
```

---

## Code Overview

```python
def main():
    note = input('Write a Note: ')

    with open('notes.txt', 'a') as file:
        file.write(note + '\n')

    print("Note saved.")


if __name__ == "__main__":
    main()
```

---

## Concepts Practiced

- Functions
- File handling
- `with open()`
- Append mode (`a`)
- User input
- Writing files
- `__name__ == "__main__"`

---

## Possible Improvements

- Read saved notes
- Delete notes
- Add timestamps
- Number each note automatically
- Create a menu system

---

## Author

Made with Python by **Parsa Seraj**