# Phone Book Dictionary 📞

A simple Python program that stores names and phone numbers in a dictionary and displays all contacts.

---

## Features

- 👤 Stores contact names
- ☎️ Stores phone numbers
- 🔁 Loops through all contacts
- 📋 Displays names with their phone numbers

---

## How It Works

The program:

1. Creates a dictionary with names and phone numbers
2. Loops through the dictionary
3. Retrieves each phone number
4. Prints the contact information

---

## Example

Input Data:

```python
phone_book = {
    'Tommy': 12345,
    'Jack': 23456,
    'Lincoln': 34567,
    'Eli': 45678,
    'Rose': 56789,
    'Emma': 67890
}
```

Output:

```text
Tommy 12345
Jack 23456
Lincoln 34567
Eli 45678
Rose 56789
Emma 67890
```

---

## Code Overview

```python
phone_book = {
    'Tommy': 12345,
    'Jack': 23456,
    'Lincoln': 34567,
    'Eli': 45678,
    'Rose': 56789,
    'Emma': 67890
}

for name in phone_book:
    number = phone_book[name]

    print(name, number)
```

---

## Concepts Practiced

- Dictionaries
- Key-value pairs
- `for` loops
- Accessing dictionary values
- Variables

---

## Possible Improvements

- Search contacts by name
- Add new contacts
- Delete contacts
- Update phone numbers
- Save contacts in a file

---

## Author

Made with Python by **Parsa**