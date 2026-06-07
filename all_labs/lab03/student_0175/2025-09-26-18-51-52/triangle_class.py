# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
def is_edge_sorted(a, b, c):
    return a <= b <= c

def classify_by_edges(a, b, c):
    if a + b <= c:
        return "invalid"
    if a == b == c:
        return "equilateral"
    if a == b or b == c or a == c:
        return "isosceles"
    return "scalene"

def classify_by_angles(a, b, c):
    if a + b <= c:
        return "invalid"
    lhs = a**2 + b**2
    rhs = c**2
    if rhs == lhs:
        return "right"
    elif rhs > lhs:
        return "obtuse"
    else:
        return "acute"
