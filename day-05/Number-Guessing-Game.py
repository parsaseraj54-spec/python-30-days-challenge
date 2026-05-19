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