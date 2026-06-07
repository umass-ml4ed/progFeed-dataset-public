# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

apples = int(input("Enter total apples: "))
baskets = int(input("Enter number of baskets: "))
numbers_per_basket = apples // baskets
leftover = apples % baskets
print(apples, "apples for")
print(baskets, "baskets can be divided as:")
print(numbers_per_basket, "apples per basket, and")
print(leftover, "leftover apples.")