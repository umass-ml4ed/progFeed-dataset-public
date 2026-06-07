# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

a = str(input("enter string a"))
b = str(input("enter string b"))
c = str(input("enter string c"))
d = str(input("enter string d"))

def useStrings():
    lst = []
    lst.append(a)
    print(lst)
    lst.append(b)
    print(lst)
    lst.insert(0,c)
    print(lst)
    lst.remove(d)
    print(lst)

    print(len(lst))

useStrings()
