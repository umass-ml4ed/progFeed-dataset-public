# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

apples = int(input("Enter total apples: "))
baskets = int(input("Enter number of baskets: "))

apples_per_basket = apples // baskets
leftover_apples = apples % baskets

print(apples,"apples")
print("for", baskets,"baskets can be divided as:")
print(apples_per_basket,"per basket, and")
print(leftover_apples,"leftover apples.")