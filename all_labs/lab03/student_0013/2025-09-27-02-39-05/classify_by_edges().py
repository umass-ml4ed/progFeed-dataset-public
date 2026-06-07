# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def classify_by_edges(a,b,c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "invalid"
    elif a == b == c:
        return " equilateral"
    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "scalene"

    