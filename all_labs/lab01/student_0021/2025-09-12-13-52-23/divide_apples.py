# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


apples = int(input("Enter the total number of apples: "))
baskets = int(input("Enter the total number of baskets "))

num1 = apples // baskets 
num2 = apples % baskets 

print (str(apples) + " apples for")
print (str(baskets) + " baskets can be divided as: ")
print (str(num1) + " apples per basket, and ")
print (str(num2) + " leftover apples. ")