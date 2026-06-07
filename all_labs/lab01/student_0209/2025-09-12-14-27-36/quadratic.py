# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
discriminant=b**2-4*a*c
root1=(-b+discriminant**0.5)/(2*a)
root2=(-b-discriminant**0.5)/(2*a)
print(str(a) + " * x^2 + " + str(b) + " * x + " + str(c) + " has roots:")
print(root1)
print(root2)