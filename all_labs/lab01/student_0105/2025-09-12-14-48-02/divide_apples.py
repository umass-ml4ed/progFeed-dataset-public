# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def divide_apples():
    apples = int(input("How many apples? "))
    baskets = int(input("How many baskets? "))
    print("Apples: " + str(apples))
    print("Baskets: " + str(baskets))
    apples_per_basket = apples // baskets
    print("Number of apples per basket: " + str(apples_per_basket))
    remainder = apples % baskets
    print("Number of apples left over: " + str(remainder))

divide_apples()