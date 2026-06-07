# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

def classify_by_edges(a, b, c):
    if a + b == c:
        return ("Right Angle Triangle")
    elif a == b == c: 
        return ("Equilateral Triangle")
    elif a == b or b == c or a == c:
        return ("Isoceles Triangle")
    else: 
        return ("Scalene Triangle")

print(classify_by_edges(a, b, c))