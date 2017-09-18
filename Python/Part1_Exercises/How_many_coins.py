coins = 0
answer = ''
while answer != 'no':
    print('You have ' + str(coins) + ' coins.')
    answer = input('Do you want another? ')
    answer = answer.lower()
    if answer == 'yes':
        coins += 1
