# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def func():

    a = input("Enter the first string (a): ")
    b = input("Enter the second string (b): ")
    c = input("Enter the third string (c): ")
    d = input("Enter the fourth string (d): ")


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

func()