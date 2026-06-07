# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_edge_sorted(a:int, b:int, c:int) ->bool:
    if a<=b and b<=c:
        return True
    else:
        return False

print(is_edge_sorted(3, 4, 5))
print(is_edge_sorted(3, 5, 3))

def classify_by_edges(a:int, b:int, c:int) ->str:
    if a+b <=c:
        return "invalid"
    elif a == b and b==c and a==c:
        return "equilateral"
    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "scalene"

def classify_by_angles(a: int, b:int, c:int) ->str:
    if a+b <=c:
        return "invalid"
    elif a**2 + b**2 == c**2:
        return "right"
    elif c**2 > a**2 + b**2:
        return "obtuse"
    else:
        return "acute"




