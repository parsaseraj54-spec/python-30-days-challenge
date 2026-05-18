name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 30:
    years_left = 30 - age
    print(f"{name}, you will turn 30 in {years_left} years.")

elif age == 30:
    print(f"{name}, you are exactly 30 years old.")

else:
    years_passed = age - 30
    print(f"{name}, you turned 30 {years_passed} years ago.")