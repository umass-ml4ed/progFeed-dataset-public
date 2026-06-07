# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
a = str(input("Enter something: "))
b = str(input("Enter something: "))
c = str(input("Enter something: "))
d = str(input("Enter something: "))

lst = []
lst.append(a)
print(lst)

lst.append(b)
print(lst)

lst.insert(0,a)
print(lst)

lst.remove(d)
print(lst)

print(len(lst))