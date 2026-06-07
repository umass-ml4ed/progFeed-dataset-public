# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

def classify_by_angles(a, b, c):
    if (a ** 2) + (b ** 2) == (c ** 2):
        return ("Right angle")
    elif (a ** 2) + (b ** 2) < (c ** 2):
        return ("Obtuse angle")
    else: 
        return ("Acute angle")

