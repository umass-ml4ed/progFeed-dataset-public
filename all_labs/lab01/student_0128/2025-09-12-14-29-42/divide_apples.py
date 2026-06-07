# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

apples = int(input("Enter total apples: "))
baskets = int(input("Enter number of baskets: "))
apples_per_basket = str(apples // baskets)
leftover_apples = str(apples % baskets)
apples = str(apples)
baskets = str(baskets)
print(apples + " apples for")
print(baskets + " baskets can be divided as:")
print(apples_per_basket + " apples per basket, and")
print(leftover_apples + " leftover apples.")