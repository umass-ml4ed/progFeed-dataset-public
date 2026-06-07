# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

number_apples = input("Enter a pos integer: ")
number_baskets = int(input("Enter a pos integer: "))
apples_per_basket = int(number_apples)//int(number_baskets)
apples_left = int(number_apples)%int(number_baskets)

print(number_apples)
print(number_baskets)
print(apples_per_basket)
print(apples_left)