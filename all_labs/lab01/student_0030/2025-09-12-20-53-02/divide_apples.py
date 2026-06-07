# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

apples =int(input("Enter number of apples :"))
baskets = int(input("Enter number of baskets :"))

apples_per_basket = apples // baskets

leftover = apples % baskets

print(str(apples)+ " apples for \n" + str(baskets) + " baskets can be divded as: \n"+ str(apples_per_basket ) + " apples per basket, and \n " + str(leftover) + " leftover apples.") 
