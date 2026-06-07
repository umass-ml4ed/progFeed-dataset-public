# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

apples = int(input("Enter total apples: "))
baskets = int(input("Enter number of baskets: "))
full_baskets = apples // baskets
remainder_apples = apples % baskets
print(str(apples) + " apples for")
print(str(baskets) + " baskets can be divided as:")
print(str(full_baskets) + " apples per basket, and")
print(str(remainder_apples) + " leftover apples.")
