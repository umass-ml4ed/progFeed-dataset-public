# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

apples = int(input("How many apples are there?\t"))

basket = int(input("How many baskets are there?\t"))

app_per_bas = str(apples // basket)

remainder = str(apples % basket)


print("There are", str(apples), "apples.")
print("There are", str(basket), "basket.")
print("There are", str(app_per_bas), "apples in each basket.")
print("There are", str(remainder), "apples left over.")