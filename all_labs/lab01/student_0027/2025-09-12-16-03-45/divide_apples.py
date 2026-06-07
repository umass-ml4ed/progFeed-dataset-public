# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

total_apples = int(input("Enter total apples: "))
baskets = int(input("Enter number of baskets: "))


apples_per_basket = total_apples // baskets
leftover = total_apples % baskets
  
print(f"{total_apples} apples for")
print(f"{baskets} baskets can be divided as:")
print(f"{apples_per_basket} apples per basket, and")
print(f"{leftover} leftover apples.")