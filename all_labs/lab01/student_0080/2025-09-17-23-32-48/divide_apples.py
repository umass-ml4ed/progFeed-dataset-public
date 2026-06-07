# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
a = input("Enter total apples ")
b = input("Enter number of baskets ")
a = int(a)
b = int(b)
c = a % b
d = (a - c) // b
aa = str(a)
bb = str(b)
cc = str(c)
dd = str(d)
print('The original number of apples ' + aa)
print('The original number of baskets ' + bb)
print('The number of apples per basket ' + dd)
print('The number of leftover apples ' + cc)