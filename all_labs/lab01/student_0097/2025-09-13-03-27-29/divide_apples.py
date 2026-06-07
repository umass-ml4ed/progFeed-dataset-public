# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

#
#
#

apples = int(input("Enter the # of apples:"))
baskets = int(input("Enter the # of baskets"))

apples_per_basket = str(apples // baskets)
apples_left_over = str(apples & baskets)

print("Apples total:", apples)
print("Baskets total:", baskets)
print("There are", apples_per_basket, "apples per basket")
print(apples_left_over , "apples remain")



