# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

apples = int(input("Enter total apples: "))
baskets = int(input("Enter number of baskets: "))

apples_per_basket = apples // baskets
leftover_apples = apples % baskets

print(
    apples,"apples for", baskets,
    "baskets can be divided as:", apples_per_basket, "per basket, and", 
    leftover_apples,"leftover apples."
)