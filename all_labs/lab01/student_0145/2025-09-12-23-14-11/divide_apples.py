 # Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

n = int (input("How many apples do you have?"))
b = int(input("How many baskets do you have?"))

e = n//b 
m = n%b
print("There are",n, "apples.")
print("There are",b, "baskets")
print("There are",e, "apples per basket.")
print("There are",m, "apples leftover")