# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

apples = int(input("Enter number of apples: "))
baskets = int(input("Enter number of baskets: "))
apples_per_basket = apples // baskets
leftovers = apples % baskets

output1 = f"{apples} apples for" 
output2 = f"{baskets} baskets can be divided as:"
output3 = f"{apples_per_basket} apples per basket, and" 
output4 = f"{leftovers} leftover apples."

print(output1)
print(output2)
print(output3)
print(output4)