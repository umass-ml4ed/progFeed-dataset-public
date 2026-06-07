# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

numApp = int(input("Enter total apples: "))
numBask = int(input("Enter number of baskets: "))
print(str(numApp) + " apples for")
print(str(numBask) + " baskets can be divided as:")
div = numApp // numBask
mod = numApp % numBask
print(str(div) + " apples per basket, and")
print(str(mod) + " leftover apples.")