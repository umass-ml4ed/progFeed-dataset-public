# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

number_of_apples = int(input("Enter the number of apples: "))
number_of_baskets = int(input("Enter the number of baskets: "))
apples_per_basket = number_of_apples // number_of_baskets 
leftover_apples = number_of_apples % number_of_baskets
print(str(number_of_apples) + " apples for ")
print(str(number_of_baskets) + " baskets can be divided as: ")
print(str(apples_per_basket) + " apples per basket, and ")
print(f"{leftover_apples} leftover apples.")