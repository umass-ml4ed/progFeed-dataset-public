# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def lst():
    lst = []
    a = input()
    b = input()
    c = input()
    d = input()
    print(a)
    print(b)
    print(c)
    print(d)
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
