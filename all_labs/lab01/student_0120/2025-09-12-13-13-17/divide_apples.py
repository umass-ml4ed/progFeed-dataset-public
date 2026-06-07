# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

number_of_apples = int(input("Enter number of apples: "))
number_of_baskets = int(input("Enter number of baskets: "))
 
apples_per_basket = number_of_apples // number_of_baskets
leftover_apples = number_of_apples % number_of_baskets

print(number_of_apples, "apples for ", number_of_baskets, "baskets can be divided as", apples_per_basket, "apples per basket and", leftover_apples, "leftover apples")
