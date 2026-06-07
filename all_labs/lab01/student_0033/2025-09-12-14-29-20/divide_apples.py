# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

num_apples=int(input("Enter total apples: "))
num_baskets=int(input("Enter number of baskets: "))
apples_per_basket=num_apples//num_baskets
leftover_apples=num_apples%num_baskets
print(num_apples,"apples for")
print(num_baskets,"baskets can be divided as:")
print(apples_per_basket,"apples per basket, and")
print(leftover_apples,"leftover apples")
