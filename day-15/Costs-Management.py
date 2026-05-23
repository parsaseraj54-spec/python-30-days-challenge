note = input('Write a Note: ')

with open('notes.txt','a') as file:
    file.write(note + '\n')
print('Note Saved')

with open ('notes.txt','r') as file:
    lines = file.readlines()
print(lines)