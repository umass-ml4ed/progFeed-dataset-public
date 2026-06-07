# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
total_apples=int(input("Enter total apples: "))
num_baskets=int(input("Enter number of baskets: "))
apples_in_each_basket=total_apples//num_baskets
leftover_apples=total_apples%num_baskets
print(total_apples,"apples for")
print(num_baskets,"baskets can be divided as:")
print(apples_in_each_basket,"apples per basket, and")
print(leftover_apples,"leftover apples.")