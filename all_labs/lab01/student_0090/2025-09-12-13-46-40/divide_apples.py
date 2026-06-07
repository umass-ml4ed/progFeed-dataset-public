# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

total_apples = int(input("Enter the amount of apples: "))
total_baskets = int(input("Enter the amount of baskets: "))

print(str(total_apples) + " apples")
print(str(total_baskets) + " baskets")

print("There are " + str(int(total_apples/total_baskets)) + " apples per basket")
print("There are " + str(total_apples%total_baskets) + " apples leftover")