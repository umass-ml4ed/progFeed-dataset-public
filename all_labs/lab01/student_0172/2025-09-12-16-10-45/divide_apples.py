# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
apples = int(input("Enter total amount of apples: "))
baskets = int(input("Enter number of baskets: "))

apples_per_each_baskets = apples // baskets
leftover = apples % baskets
print(str(apples) + " apples for")
print(str(baskets) + " basket can be divided as: ")
print(str(apples_per_each_baskets) + " apples per basket, and")
print(str(leftover) + " leftover apples")