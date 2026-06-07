# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

total_apples = int(input("Enter total apples: "))
total_baskets = int(input("Enter number of baskets: "))
apples_per_basket = total_apples//total_baskets
remainder = total_apples%total_baskets
print(str(total_apples) + " apples for\n" + str(total_baskets) + " baskets can be divided as:\n" + str(apples_per_basket) + " apples per basket, and\n" + str(remainder) + " leftover apples.")