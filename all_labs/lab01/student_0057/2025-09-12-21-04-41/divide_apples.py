# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

a = int(input("Enter total apples: "))
b = int(input("Enter number of baskets: "))
print(a, "apples for")
print(b, "baskets can be divided as")
a_per_b = a // b
leftover = a % b
print(a_per_b, "apples per basket, and")
print(leftover, "leftover apples.")