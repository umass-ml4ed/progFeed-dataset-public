# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

total_apples = int(input("Enter total apples: "))
total_baskets = int(input("Enter number of baskets: "))

apple_per_basket = total_apples // total_baskets
leftover = total_apples % total_baskets

print(f"{total_apples} apples for")
print(f"{total_baskets} baskets can be divided as:")
print(f"{apple_per_basket} apples per basket, and")
print(f"{leftover} leftover apples.")