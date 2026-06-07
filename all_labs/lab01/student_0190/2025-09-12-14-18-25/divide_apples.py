# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

total_apples = int(input("Enter total apples: "))
num_baskets = int(input("Enter number of baskets: "))
apples_per_basket = total_apples // num_baskets
leftover_apples = total_apples % num_baskets
print(f"{total_apples} apples for")
print(f"{num_baskets} baskets can be divded as:")
print(f"{apples_per_basket} apples per basket, and")
print(""f"{leftover_apples} leftover apples")