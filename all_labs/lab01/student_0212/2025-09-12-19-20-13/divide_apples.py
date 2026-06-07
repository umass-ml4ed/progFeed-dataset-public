# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

apples = input("Enter total apples: ")
baskets = input("Enter number of baskets: ")

print(apples + " apples for")
print("\t" + baskets + " baskets can be divided as:")
print(str(int(apples) // int(baskets)) + " apples per basket, and")
print(str(int(apples) % int(baskets)) + " leftover apples.")

