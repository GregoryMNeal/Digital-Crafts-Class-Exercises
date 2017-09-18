secret_number = 5
print('I am thinking of a number between 1 and 10.')
answer = ''
while answer != secret_number:
    answer = int(input('What\'s the number? '))
    if answer == secret_number:
        print('You win!')
    else:
        print('Nope, try again.')
