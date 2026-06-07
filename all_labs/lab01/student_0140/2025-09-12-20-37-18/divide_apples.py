# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

total = int(input("Enter total apples"))
baskets = int(input("Enter number of baskets"))

def divide_apples(totals, baskets):
    return totals // baskets
print(divide_apples(total, baskets))

def remainder(apples, baskets):
    return apples % baskets

print(total, "apples for")
print(baskets, "baskets can be divided as")
print(divide_apples(total, baskets), "apples per basket")
print(remainder(total, baskets), "leftover apples")