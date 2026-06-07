# AUTHOR   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_edge_sorted(a,b,c):
    if a<=b and b<=c:
        return True
    else:
        return False
def classify_by_edges(a,b,c):
    if a+b<=c:
        return 'invalid'
    elif a==b and b==c and c==a:
        return 'equilateral'
    elif a!=b and b!=c and c!=a:
        return 'scalene'
    else:
        return 'isosceles'

def classify_by_angles(a,b,c):
    if a+b<=c:
        return 'invalid'
    elif a**2+b**2==c**2:
        return 'right'
    elif a**2+b**2<c**2:
        return 'obtuse'
    else:
        return 'acute'

