# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
import math
apples = int(input("Enter total apples: "))
baskets = int(input("Enter number of baskets: "))
print(f"{apples} apples for\n{baskets} baskets can be divided as:\n{math.floor(apples/baskets)} apples per basket, and\n{apples%baskets} leftover apples.")