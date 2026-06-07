# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


apple = int(input("Enter total number of apples: "))
basket = int(input("Enter number of baskets: "))

apple_per_basket = apple//basket
leftover_apple = apple%basket

print("You have", apple, "apples and,")
print(basket, "baskets.")
print(apple_per_basket, "apples per basket.")
print(leftover_apple, "leftover apples.")