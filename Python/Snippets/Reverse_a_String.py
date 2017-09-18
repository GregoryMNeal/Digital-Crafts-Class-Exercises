myString = input("Please enter a string: ")

revList = []
for char in reversed(myString):
    revList.append(char)

prtString = ''.join(revList)
print(prtString)
