# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

SnoApples = input("Enter number of apples: ")
SnoBaskets = input("Enter number of baskets: ")
noApples = int(SnoApples)
noBaskets = int(SnoBaskets)
PerBasket = noApples//noBaskets
Reminder = noApples%noBaskets

print("there are", noApples)
print("for", noBaskets, "baskets")
print("meaning", PerBasket,"Apples per basket")
print("and", Reminder,"leftover.")