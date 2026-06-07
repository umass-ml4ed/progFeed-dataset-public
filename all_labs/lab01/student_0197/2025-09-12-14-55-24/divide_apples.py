# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

Apples = input("Enter total number of apples: ")

Baskets = input("Enter total number of baskets: ")

Answer = int(Apples) / int(Baskets)
Remainder = int(Apples) % int(Baskets)

print(
	Apples + " apples for\n" + 
	Baskets + " baskets can be divided as:\n" + 
	str(Answer) + " apples per basket, and\n" + 
	str(Remainder) + " leftover apples."
	)