day = int(input('Day (0-6) '))

if day == 1 or day == 2 or day == 3 or day == 4 or day == 5:
  print("Go to work")
elif day == 0 or day == 6:
  print("Sleep in")
else:
  print("That is not a valid day.  At least not on planet Earth.")
