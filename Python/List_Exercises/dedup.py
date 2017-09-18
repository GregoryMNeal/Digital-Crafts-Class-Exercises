# Imports

# Functions

def remove_dup():
    duplist = [1,1,2,3,3,4,5,5,6,7,7,8,9,9,10]
    newlist = []
    # iterate though duplicate list
    for x in range(0, len(duplist)):
    # check new list for the value
        found = ''
        for y in range(0, len(newlist)):
            if duplist[x] == newlist[y]:
                found = 'Y'
                break
    # Add the value to the new list if not found to already exist
        if found != 'Y':
            newlist.append(duplist[x])
    print (str(newlist))

# Main

if __name__ == "__main__":

    remove_dup()
