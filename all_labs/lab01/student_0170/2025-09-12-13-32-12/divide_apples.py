# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

apples = int(input("Enter total apples: "))
baskets = int(input("Enter number of baskets: "))
applesPer = apples//baskets
applesLeft = apples%baskets
print(f"{apples} apples for \n {baskets} baskets can be divided as:\n {applesPer} apples per basket, and\n {applesLeft} leftover apples.")