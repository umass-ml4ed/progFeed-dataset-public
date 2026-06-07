# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

ap= input("Enter Total Apples: ")
ba= input("Enter Total Baskets: ")

print(ap, "apples for")
print(ba, "baskets can be devided as: ")

div= int(ap)//int(ba)
print(div, "apples per basket, and")

rem= int(ap)%int(ba)
print(rem, "leftover apples.")