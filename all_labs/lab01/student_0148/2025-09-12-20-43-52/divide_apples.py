# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

apples = int(input("Enter total apples: "))
baskets = int(input("Enter number of baskets: "))

apb = apples // baskets
r = apples % baskets

print(str(apples) +" apples for \n" +  str(baskets) + " baskets can be divided as:")
print(str(apb) + " apples per basket, and \n " + str(r) + " leftover apples.")
