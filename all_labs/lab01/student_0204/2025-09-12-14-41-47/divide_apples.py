# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

while True:
    try:
        totalApples = int(input("Number of apples: "))
        if totalApples >= 0:
            break
        else:
            raise ValueError()
    except ValueError:
        print("The number of apples must be a positive integer")

while True:
    try:
        numberOfBaskets = int(input("Number of baskets: "))
        if numberOfBaskets >= 0:
            break
        else:
            raise ValueError()
    except ValueError:
        print("The number of baskets must be a positive integer")

applesPerBasket = totalApples // numberOfBaskets
leftoverApples = totalApples % numberOfBaskets

print(str(totalApples) + " apples for")
print(str(numberOfBaskets) + " baskets can be divided as:")
print(str(applesPerBasket) + " apples per basket, and")
print(str(leftoverApples) + " leftover apples.")


