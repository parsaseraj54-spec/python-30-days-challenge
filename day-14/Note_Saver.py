def main():
    note = input('Write a Note: ')  # Prompt the user to enter a note and store the input as a string in the variable 'note'
    with open('notes.txt', 'a') as file:  # Open the file 'notes.txt' in append mode ('a'); if the file doesn't exist, create it
        file.write(note + '\n')  # Write the user's note to the file, adding a newline character to separate each note on a new line
    print("Note saved.")  # Inform the user that the note has been successfully saved

if __name__ == "__main__":
    main()  # If this script is run directly (not imported), call the main() function to execute the program
