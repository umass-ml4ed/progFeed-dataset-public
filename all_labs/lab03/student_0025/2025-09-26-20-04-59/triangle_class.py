# Author   : REDACTED
# Emails    : REDACTED
# Spire ID : REDACTED

# Implement the two functions below:
# is_edge_sorted
# classify_by_edges

# ----- YOUR CODE STARTS HERE -----
def is_edge_sorted(a, b, c):
  if a <= b <= c:
    return True
  else:
    return False
def classify_by_edges(a, b, c):
  if a + b <= c:
    return "invalid"
  elif a == b == c:
    return "equilateral"
  elif a == b or b == c or a == c:
    return "isosceles"
  else:
    return "scalene"
  

# ===== YOUR CODE ENDS HERE =====

# You can use the code below to help test your functions

# Uncomment the following 5 lines (i.e. remove the starting # characters on each line) to test is_edge_sorted
print(is_edge_sorted(3, 4, 5)) # should print True
print(is_edge_sorted(3, 3, 3)) # should print True
print(is_edge_sorted(3, 2, 4)) # should print False
print(is_edge_sorted(2, 5, 3)) # should print False
print(is_edge_sorted(3, 5, 3)) # should print False

# This is utility function. Do NOT modify this function
def print_triangle_class(a, b, c):
  if is_edge_sorted(a, b, c):
    triangle_class = classify_by_edges(a, b, c)
  else:
    triangle_class = "not edge sorted"
  print(f'Triangle ({a}, {b}, {c}) is {triangle_class}')

# Uncomment the following 6 lines (i.e. remove the starting # characters on each line) to test classify_by_edges
print_triangle_class(3, 4, 8) # invalid
print_triangle_class(3, 4, 5) # scalene
print_triangle_class(3, 3, 3) # equilateral
print_triangle_class(5, 5, 6) # isosceles
print_triangle_class(5, 6, 6) # isosceles
print_triangle_class(1, 2, 3) # invalid