# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

total_apples = int(input("Enter total apples:"))
number_of_baskets = int(input("Enter number of baskets:"))
apples_per_basket = total_apples // number_of_baskets
apples_leftover = total_apples % number_of_baskets
print(f"{total_apples} apples for")
print(f"{number_of_baskets} baskets can be divided as:")
print(f"{apples_per_basket} apples per basket, and")
print(f"{apples_leftover} leftover apples.")