# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

w = input("Enter total apples: ")
b = input("Enter number of baskets: ")

c = int(w)//int(b)
d = int(w)%int(b)

print(w, "apples for\n" + b, "baskets", "can be divided as:\n" + str(c), " apples per basket, and\n" + str(d), " leftover apples.")

