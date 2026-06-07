# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
totA = int(input("Enter the number of apples: "))
totB = int(input("Enter the number of baskets: "))

print(str(totA) + " apples for")
print(str(totB) + " baskets can be divided as:")
assign = (totA // totB)
print(str(assign) + " apples per basket, and")


leftover = (totA % totB)
print (str(leftover) + " leftover apples.")

