# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

a = input("Enter the string a:")
b = input("Enter the string b:")
c = input("Enter the string c:")
d = input("Enter the string d:")

list = []

list.append(a)
print(list) 

list.append(b)
print(list)

list.insert(0, c)
print(list)

list.remove(d)
print(list)

print(len(list))