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

def classify_by_angles(a,b,c):
    if a + b <= c:
        return "invalid"
    if c**2 == a**2 + b**2:
        return "right"
    if c**2 >= a**2 + b**2:
        return "obtuse"
    else:
        return "acute"

    


        
    

    #if the square of c equals the sum of the squares of a and b, the triangle is right. If the square of c is greater than the sum of the squares of a and b, the triangle is obtuse. Otherwise, if the square of c is smaller, the triangle is acute.
