# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

# The task of this program is to read in two inputs from the user, store each in a separate variable:
# The total number of apples (a positive integer)
# The number of baskets (a positive integer)

apples = int(input("Enter total apples: "))
baskets = int(input("Enter number of baskets: "))

per = apples // baskets
left = apples % baskets

print(str(apples) + " apples for")
print(str(baskets) + " baskets can be divided as:")
print(str(per) + " apples per basket, and")
print(str(left) + " leftover apples.")