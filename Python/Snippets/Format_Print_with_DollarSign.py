total_bill = float(input('Please enter total bill amount: '))
level_of_service = input('Please enter level of service - (Good) (Fair) (Bad): ')
level_of_service = level_of_service.lower()

tip = 0
if level_of_service == 'good':
    tip = total_bill * .2
elif level_of_service == 'fair':
    tip = total_bill * .15
elif level_of_service == 'bad':
    tip = total_bill * .10

total_bill = total_bill + tip

print('Tip amount: ' + "${:.2f}".format(tip))
print('Total amount: ' + "${:.2f}".format(total_bill))
