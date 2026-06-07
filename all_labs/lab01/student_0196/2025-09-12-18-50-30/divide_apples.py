# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

totalApples = int(input("Enter total apples: "))

totalBaskets = int(input("Enter total number of baskets: "))

applesInBasket = totalApples // totalBaskets

leftOverApples = totalApples % totalBaskets

print(str(totalApples) + " apples for ")
print(str(totalBaskets) + " baskets can be divided as: ")
print(str(applesInBasket) + " apples per basket, and ")
print(str(leftOverApples) + " leftover apples.")