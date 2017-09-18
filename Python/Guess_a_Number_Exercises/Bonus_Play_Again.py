import random

print('I am thinking of a number between 1 and 10.')

while True:
    random_number = random.randint(1, 10)
    # You get 5 chances to guess correctly
    guesses = 5
    answer = ''
    while True:
        print('You have ' + str(guesses) + ' guesses left.')
        answer = int(input('What\'s the number? '))
        guesses = guesses - 1
        if answer == random_number:
            print('Yes!  You win!')
            break
        elif guesses == 0:
            print('You ran out of guesses!')
            break
        elif answer < random_number:
            print(str(answer) + ' is too low.')
        elif answer > random_number:
            print(str(answer) + ' is too high.')
    # Would you like to play again?
    play = input('Do you want to play again (Y or N)? ')
    play = play.upper()
    if play != 'Y':
        break
