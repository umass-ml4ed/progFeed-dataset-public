# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

apples = (input("Enter total apples: "))
baskets = (input("Enter number of baskets: "))
quotient = (int(apples) / int(baskets))
remainder = int(apples) % int(baskets)

print(apples + " apples for")
print(baskets + " baskets can be divided as:")
print(str(int(quotient)) + " apples per basket, and")
print(str(remainder) + " leftover apples.")