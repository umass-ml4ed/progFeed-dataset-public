# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_edge_sorted(a: float, b: float, c: float):
    if a <= b and b <= c:
        return True
    else:
        return False

def classify_by_edges(a: float, b: float, c: float):
    AddA_B = a + b
    if AddA_B <= c:
        return "invalid"
    elif a == b and b == c:
        return "equilateral"
    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "scalene"

def classify_by_angles(a: float, b: float, c: float):
    AddA_B = a + b
    cc = c * c
    aa = a * a
    bb = b * b
    aabb = aa + bb
    if AddA_B <= c:
        return "invalid"
    elif cc == aabb:
        return "right"
    elif cc > aabb:
        return "obtuse"
    elif cc < aabb:
        return "acute"

def print_triangle_class(a, b, c, f):
  print(f'Triangle ({a}, {b}, {c}) is {"not edge sorted" if not is_edge_sorted(a, b, c) else f(a, b, c)}')
