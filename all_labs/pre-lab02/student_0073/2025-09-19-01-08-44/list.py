# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def lst():
    a = str("Hello")
    b = str("Hola")
    c = str("Namaste")
    d = str("Hola")
    lst = []
    lst.append(a)
    print(lst)
    lst.append(b)
    print(lst)
    lst.insert(0, c)
    print(lst)
    lst.remove(d)
    print(lst)
    print(len(lst))
    return lst
lst()