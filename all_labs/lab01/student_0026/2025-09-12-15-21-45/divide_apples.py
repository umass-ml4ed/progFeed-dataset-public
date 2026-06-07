# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

total_apples=(int(input("Enter total apples:")))
total_baskets=(int(input("Enter number of baskets:")))
apples=total_apples//total_baskets
leftover_apples=total_apples%total_baskets
print(total_apples, "apples for")
print(total_baskets,"baskets can be divided as:")
print(apples, "apples per basket, and")
print(leftover_apples, "leftover apples.")