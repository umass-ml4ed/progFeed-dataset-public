# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

numApples = (input("Enter total apples"))
numBaskets = (input("Enter number of baskets"))

print(numApples + " apple for ")
print(numBaskets + "baskets can be divided as:")
print(int(numApples) // int(numBaskets) , "apples per basket, and")
print(int(numApples) % int(numBaskets) , "leftover apples.")