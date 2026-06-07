# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

aplz = input("Total apples?")
bskz = input("Number of baskets?")
aeb = (int(aplz) // int(bskz))
alb = (int(aplz) % int(bskz))

print(aplz + " apples for")
print(bskz + " baskets can be divided for:")
print(int(aeb), " apples per basket and")
print(int(alb), " leftover apples.")