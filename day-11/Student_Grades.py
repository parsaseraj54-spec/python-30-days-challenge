grades = { 'Jack' : 96 , 'Sam': 58 , 'Ema': 78 , 'Ana': 99}

best_student = ''
best_grade = 0

for student, grade in grades.items():
    if grade > best_grade:
        best_grade = grade
        best_student = student

print('Best Student', best_student)
print('Best Grade', best_grade)