# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
a = input()
b = input()
c = input()
d = input()
lst = []
lst.append(a)
print(lst)
lst.append(b)
print(b)
lst.insert(0, c)
print(lst)
if d in lst:
    lst.remove(d)
    print(lst)
    print(len(lst))
else:
    print(lst)
    print(len(lst))