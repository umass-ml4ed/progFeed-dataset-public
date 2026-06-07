# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

a = int(input("Enter total apples: "))
b = int(input("Enter number of baskets: "))

per = a // b
leftover = a % b

print(a, "apples for")
print(b, "baskets can be divided as:")
print(per, "apples per basket, and")
print(leftover, "leftover apples.")