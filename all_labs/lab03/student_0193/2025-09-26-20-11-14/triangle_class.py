# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_edge_sorted(a: float, b: float, c: float):
    if a <= b and b <= c:
        return True
    else:
        return False


def print_triangle_class(a, b, c, f):
  print(f'Triangle ({a}, {b}, {c}) is {"not edge sorted" if not is_edge_sorted(a, b, c) else f(a, b, c)}')
