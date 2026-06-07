# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
apples = input("Enter total apples : ")
baskets = input("Enter number of baskets : ")
applesPerBasket = int(apples) // int(baskets)
applesLeftover = int(apples) % int(baskets)
print(apples +" apples for")
print(baskets + " baskets can be divided as: ")
print(str(applesPerBasket) + " apples per basket, and ")
print(str(applesLeftover) + " leftover apples.")