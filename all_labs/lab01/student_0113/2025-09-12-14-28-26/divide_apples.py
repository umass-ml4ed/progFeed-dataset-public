#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

apples = int(input("Enter the total number of apples: "))
baskets = int(input("Enter the number of baskets: "))

apples_per_baskets = apples // baskets 
leftover = apples % baskets
print(str(apples) + " apples for \n" + str(baskets) + " baskets can be divided as: ")
print(str(apples_per_baskets) + " apples per basket, and \n" + str(leftover) + " leftover apples")