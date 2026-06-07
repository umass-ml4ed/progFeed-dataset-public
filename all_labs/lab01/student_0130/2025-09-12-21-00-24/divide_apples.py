#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

a=int(input("Enter total apples:"))
b=int(input("Enter number of baskets:"))

a_per_b = a // b
leftover_a = a % b 

print(str(a)+ ("apples for"))
print(str(b)+ ("baskets can be divided as:"))
print(str(a_per_b) + (" apples per basket,and"))
print(str(leftover_a)+ ("leftover apples."))