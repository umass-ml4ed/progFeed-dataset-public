# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

apples = int(input("Enter number of apples: "))
baskets = int(input("Enter number of baskets: "))

apples_per_basket = apples // baskets
leftover_apples = apples % baskets

print(f"{apples} apples for\n{baskets} baskets can be divided as:\n {apples_per_basket} apples per basket, and\n {leftover_apples} leftover apples.")