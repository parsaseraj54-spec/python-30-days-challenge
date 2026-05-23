# Notes Saver & Reader 📝📖

A simple Python application that allows users to save notes and read all saved notes from a text file.

---

## Features

- ✍️ Write notes
- 💾 Save notes to a file
- 📂 Automatically creates a file if needed
- 📖 Read previously saved notes
- ➕ Keep old notes while adding new ones

---

## How It Works

The program:

1. Takes a note from the user
2. Opens `notes.txt` in append mode
3. Saves the note into the file
4. Displays a confirmation message
5. Opens the file again in read mode
6. Reads all notes
7. Displays the stored notes

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
Write a Note: Study Python loops
```

Output:

```text
Note Saved

['Study Python loops\n']
```

---

## Code Overview

```python
note = input('Write a Note: ')

with open('notes.txt','a') as file:
    file.write(note + '\n')

print('Note Saved')

with open('notes.txt','r') as file:
    lines = file.readlines()

print(lines)
```

---

## Concepts Practiced

- User input
- File handling
- `with open()`
- Append mode (`a`)
- Read mode (`r`)
- `readlines()`
- Variables

---

## Possible Improvements

- Display notes line by line instead of a Python list

```python
for line in lines:
    print(line)
```

- Add note numbering
- Delete notes
- Add timestamps
- Create a menu system

---

## Author

Made with Python by **Parsa Seraj**