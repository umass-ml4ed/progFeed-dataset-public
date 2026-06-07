# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

total_apples = int(input("Enter total apples: "))
Baskets = int(input("Enter number of baskets: "))
apples_per_basket = total_apples//Baskets
Left_over_apples = total_apples%Baskets
print(f"{total_apples} apples for\n{Baskets} baskets can be divided as:\n{apples_per_basket} apples per basket,and\n{Left_over_apples} left over apples.")