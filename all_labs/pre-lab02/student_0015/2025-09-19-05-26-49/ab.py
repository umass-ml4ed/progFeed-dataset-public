# Author: REDACTED
# Email: REDACTED
# SPIRE ID: REDACTED

# Take input from user a and b, print a number b times and b number a times
a = int(input('Enter first integer (a): '))
b = int(input("Enter second integer (b): "))

# Make sure to typecast so it doesnt get xplied
pattern= str(a)*b + str(b)*a
print(pattern)
