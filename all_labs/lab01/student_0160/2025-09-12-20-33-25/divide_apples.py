# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

totalNoOfApples = int(input("What is the total number of Apples?"))
numberOfBaskets = int(input("What is the number of Baskets?"))

calculateApplesPerBasket = totalNoOfApples // numberOfBaskets
calculateApplesLeftOver = totalNoOfApples % numberOfBaskets

print(str(totalNoOfApples) + " Baskets for")
print(str(numberOfBaskets) + " Apples can be divided as:")
print(str(calculateApplesPerBasket) + " Apples per Basket, and")
print(str(calculateApplesLeftOver) + " leftover Apples.")