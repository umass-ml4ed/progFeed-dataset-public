# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

num_apples = int(input("Enter total apples: "))
num_baskets = int(input("Enter number baskets: "))

apples_per_basket = num_apples//num_baskets
leftover = num_apples%num_baskets

print(f"{num_apples}\n{num_baskets}\n{apples_per_basket}\n{leftover}")