# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

apples = input('Enter total apples: ')
baskets = input('Enter total baskets: ')
apples_per_basket = int(apples)//int(baskets)
leftovers = int(apples)%int(baskets)
print (apples + ' apples for')
print(baskets + ' can be divided as:')
print(str(apples_per_basket) + ' apples per basket, and')
print(str(leftovers) + ' leftover apples.')