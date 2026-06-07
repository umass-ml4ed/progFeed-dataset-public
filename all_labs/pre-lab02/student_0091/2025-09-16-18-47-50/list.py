# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED



def useStrings():
    a = str(input("enter string 1"))
    b = str(input("enter string 2"))
    c = str(input("enter string 3"))
    d = str(input("enter string 4"))
    lst = []
    lst.append(a)
    print(lst)
    lst.append(b)
    print(lst)
    lst.insert(0,c)
    print(lst)
    lst.remove(b)
    print(lst)

    print(len(lst))

useStrings()
