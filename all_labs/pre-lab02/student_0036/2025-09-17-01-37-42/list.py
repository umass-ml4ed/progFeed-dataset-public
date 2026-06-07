# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def list():
    a=input("A string: ")
    b=input("A string: ")
    c=input("A string: ")
    d=input("A string: ")
    lst=[]
    lst.append(a)
    print(lst)
    lst.append(b)
    print(lst)
    lst.insert(0,c)
    print(lst)
    lst.remove(d)
    print(lst)
    print(len(lst))
list()