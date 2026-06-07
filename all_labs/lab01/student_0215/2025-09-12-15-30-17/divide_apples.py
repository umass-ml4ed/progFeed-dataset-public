# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

ap = input("Enter total apples: ")
bas = input("Enter number of baskets: ")
baskets = int(bas)
apples = int(ap)
print(ap, "apples for")
print(bas, "baskets can be divided as:")
first = apples // baskets
second = apples % baskets
print(first, "apples per basket, and")
print(second, "leftover apples.")