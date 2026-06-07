# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def divide_apples(apples, baskets):
    apples_per_basket = apples // baskets
    leftover_apples = apples % baskets
    print(apples, "apples for\n" + str(baskets), "baskets can be divided as:\n" + str(apples_per_basket) , "apples per basket, and\n" + str(leftover_apples) , "leftover apples.")

apples = int(input("Enter total apples: "))
baskets = int(input("Enter total baskets: "))
divide_apples(apples,baskets)