# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

a = input("Words here! ")
b = input("More words here! ")
c = input("Even more words here! ")
d = input("Extra words here! ")
print(a)
print(b)
print(c)
print(d)
lst = []
def add_end(words):
    lst.append(words)
    print(lst)
add_end(a)
add_end(b)
add_end(c)
lst.remove(d)
print(lst)
print(len(lst))