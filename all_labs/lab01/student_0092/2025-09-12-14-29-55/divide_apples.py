# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

apples = input("Enter total apples: ")
baskets = input("Enter number of baskets: ")
apb = int(apples) // int(baskets)
rem = int(apples) % int(baskets)
print(apples + " apples for\n" + baskets + " can be divided as:\n" + str(apb) + " apples per basket, and\n" + str(rem) + " leftover apples.")