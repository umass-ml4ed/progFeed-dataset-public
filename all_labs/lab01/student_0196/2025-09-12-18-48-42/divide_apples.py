# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

totalApples = int(input("Enter total apples: "))

totalBaskets = int(input("Enter total number of baskets: "))

applesInBasket = totalApples // totalBaskets

leftOverApples = totalApples % totalBaskets

print(str(totalApples) + " apples for " + str(totalBaskets) + " baskets can be divided as: " + str(applesInBasket) + " apples per basket, and " + str(leftOverApples) + " leftover apples.")