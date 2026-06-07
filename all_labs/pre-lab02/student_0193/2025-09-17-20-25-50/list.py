# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

a = str(input("a: "))
b = str(input("b: "))
c = str(input("c: "))
d = str(input("d: "))

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