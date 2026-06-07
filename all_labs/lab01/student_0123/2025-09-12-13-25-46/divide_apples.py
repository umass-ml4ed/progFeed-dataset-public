# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

total_apples = int(input("Enter total apples: "))
total_baskets = int(input("Enter number of baskets: "))
apples_per_basket = total_apples // total_baskets
leftover_apples = total_apples % total_baskets

print(total_apples, "apples for")
print(total_baskets, "baskets can be divided as:")
print(int(apples_per_basket), "apples per basket, and")
print(int(leftover_apples), "leftover apples.")