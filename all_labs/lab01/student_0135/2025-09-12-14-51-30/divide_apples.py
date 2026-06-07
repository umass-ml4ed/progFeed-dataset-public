# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

tot = int(input("Enter the number of apples: "))
bask = int(input("Enter the number of baskets: "))
apples_per_basket = tot // bask
leftover_apples = tot % bask

print(str(tot) + " apples for ")
print(str(bask) + " baskets can be divided as: ")
print(str(apples_per_basket) + " apples per basket, and")
print(str(leftover_apples) + " leftover apples.")

