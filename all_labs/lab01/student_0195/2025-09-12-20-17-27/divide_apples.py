# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

apples = int(input("Enter number of apples: "))
baskets = int(input("Enter number of baskets: "))

AperB = apples//baskets
leftover = apples % baskets

print(str(apples) + " apples and ")
print(str(baskets) + " baskets")
print(str(AperB) + " apples per basket with")
print(str(leftover) + " apples leftover")