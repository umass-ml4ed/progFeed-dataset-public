# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

x = int(input("How many apples: "))
y = int(input("How many baskets: "))
applesinbasket = x//y
leftoverapples = x%y

print ("Original apples: "+str(x))
print ("original baskets: "+str(y))
print ("apples per basket: "+str(applesinbasket))
print ("leftover apples: "+str(leftoverapples))