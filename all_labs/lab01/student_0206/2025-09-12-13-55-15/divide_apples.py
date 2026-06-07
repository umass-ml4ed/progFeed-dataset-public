# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

apples = int(input("Enter total apples: "))
baskets = int(input("Enter number of baskets: "))
app_per_bask = apples//baskets
app_left = apples%baskets
print(f"""{apples} apples for 
{baskets} baskets can be divided as: 
{app_per_bask} apples per basket, and 
{app_left} leftover apples.""")