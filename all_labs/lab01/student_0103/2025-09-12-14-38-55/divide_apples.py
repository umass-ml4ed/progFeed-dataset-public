# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

str_apples = input("Enter total apples: ")
str_baskets = input("Enter number of baskets: ")
apples = int(str_apples)
baskets = int(str_baskets)
apples_per_basket = apples // baskets
leftover_apples = apples % baskets
str_apples_per_basket = str(apples_per_basket)
str_leftover_apples = str(leftover_apples)
print(str_apples, "apples for")
print(str_baskets, "can be divided as:")
print(str_apples_per_basket, "apples per basket, and")
print(str_leftover_apples, "leftover apples.")