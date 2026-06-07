# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

numapples = input("Enter total apples: ")
numbaskets = input("Enter total baskets: ")
div = (int(numapples) // int(numbaskets))
mod = (int(numapples) % int(numbaskets))
print(f"{numapples} apples for")
print(f"{numbaskets} baskets can be divided as:")
print(f"{div} apples per basket, and")
print(f"{mod} leftover apples.")
