# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

t= int(input("Enter total apples: "))
b= int(input("Enter number of baskets: "))

apples_per_basket= t//b
r_apples= t%b

print(f"{t} apples for")
print(f"{b} baskets can be divided as: ")
print(f"{apples_per_basket} apples per basket, and")
print(f"{r_apples} leftover apples.")
