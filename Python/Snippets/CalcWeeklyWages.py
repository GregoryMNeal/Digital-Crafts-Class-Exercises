# Function requirements:
#   Calculate total pay for the week given a person's work hours for the week and their hourly wage.
#   Any hours worked over 40 are paid at 1.5 times the hourly wage.

def calcWeeklyWages(totalHours, hourlyRate):
    overtimeHours = totalHours - 40
    overtimeRate = hourlyRate * 1.5
    regularPay = hourlyRate * 40
    overtimePay = overtimeHours * overtimeRate
    totalPay = regularPay + overtimePay
    return totalPay

totalPay = calcWeeklyWages(50.5, 10.25)

print(totalPay)
