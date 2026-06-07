# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED




def is_edge_sorted(a, b, c):
    if a <= b and b <= c:   
        return True
    else:
        return False






def classify_by_edges(a,b,c):
    if a + b <= c:
        return "invalid"
    elif a == b == c:
        return "equilateral"
    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "scalene"

    