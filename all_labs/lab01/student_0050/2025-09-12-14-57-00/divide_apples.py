# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

total = int(input("What is the total number of apples?: "))
baskets = int(input("What is the number of baskets?: "))

leftover = total%baskets
amtbasket = total//baskets

print(f"{total} apples for \n{baskets} can be divided as: \n{amtbasket} apples per basket, and \n{leftover} leftover apples.")