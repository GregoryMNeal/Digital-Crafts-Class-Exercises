import random

random_number = random.randint(1, 10)

print('I am thinking of a number between 1 and 10.')
answer = ''
while answer != random_number:
    answer = int(input('What\'s the number? '))
    if answer == random_number:
        print('You win!')
    elif answer < random_number:
        print(str(answer) + ' is too low.')
    elif answer > random_number:
        print(str(answer) + ' is too high.')
