# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_edge_sorted(a, b, c):
  return a <= b <= c 

def classify_by_edges(a, b, c):
  if a + b <= c:
    return ("invalid")
  elif a == b == c:
    return ("equilateral")
  elif a == b or b == c or a == c:
    return ("isosceles")
  else: 
    return ("scalene")

def classify_by_angles(a, b, c):
  if (a + b) <= c:
    return ("invalid")
  elif (c ** 2) == (a ** 2) + (b ** 2):
    return ("right")
  elif (c ** 2) >= (a ** 2) + (b ** 2):
    return ("obtuse")
  else: 
    return ("acute")

def print_triangle_class(a, b, c, f):
  print(f'Triangle ({a}, {b}, {c}) is {"not edge sorted" if not is_edge_sorted(a, b, c) else f(a, b, c)}')




print(is_edge_sorted(3, 4, 5))  
print(is_edge_sorted(3, 3, 3))  
print(is_edge_sorted(3, 2, 4))  
print(is_edge_sorted(2, 5, 3))  
print(is_edge_sorted(3, 5, 3))  


print_triangle_class(3, 4, 7, classify_by_angles)  
print_triangle_class(3, 4, 5, classify_by_angles)  
print_triangle_class(3, 3, 3, classify_by_angles)  
print_triangle_class(2, 3, 4, classify_by_angles)  
print_triangle_class(4, 5, 6, classify_by_angles)  
print_triangle_class(5, 12, 13, classify_by_angles)  


print_triangle_class(3, 4, 8, classify_by_edges)  
print_triangle_class(3, 4, 5, classify_by_edges)  
print_triangle_class(3, 3, 3, classify_by_edges)  
print_triangle_class(5, 5, 6, classify_by_edges)  
print_triangle_class(5, 6, 6, classify_by_edges)  
print_triangle_class(1, 2, 3, classify_by_edges)  