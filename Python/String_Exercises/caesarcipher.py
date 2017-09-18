# Import ASCII letters
import string
astring = string.ascii_letters
astring = astring.upper()
alist = list(astring)

# Functions

def decrypt_msg(emsg):
    emsg = emsg.upper()
    elist = list(emsg)
    # Decrypt the message into a list
    dlist = []
    for x in range(0, len(elist)):
        found = ''
        for y in range(0, len(alist)):
            if elist[x] == alist[y]:
                found = 'Y'
                newletter = alist[y + 13]
                dlist.append(newletter)
                break
        if found != 'Y':
            dlist.append(elist[x])
    dstring = ''.join(dlist)
    pstring = dstring.capitalize()
    print(pstring)

# Main

if __name__ == "__main__":

    # Receive encrypted message
    emsg = input("Please enter the encrypted message: ")
    decrypt_msg(emsg)
