# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
# Date     : 2024-10-03

applesTotal = int(input("Enter the total number of apples: "))
basketsTotal = int(input("Enter the total number of baskets:"))

applesBasket = applesTotal // basketsTotal
applesLeft = applesTotal % basketsTotal
print("Each basket will have", applesBasket, "apples")
print("There will be", applesLeft, "apples left over")