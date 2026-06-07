# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

apples = int(input("Enter total apples: "))
baskets = int(input("Enter number of baskets: "))

def divide_apples(apples, baskets):
    apples_per_basket = apples // baskets
    apples_leftover = apples % baskets
    return (apples_per_basket, apples_leftover)

apples_per_basket, apples_leftover = divide_apples(apples, baskets)

print (apples, "apples for")
print (baskets, "baskets can be divided as:")
print (apples_per_basket, "apples per basket, and")
print (apples_leftover, "leftover apples.")
