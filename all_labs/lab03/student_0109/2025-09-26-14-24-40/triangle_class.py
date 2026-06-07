#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

# Implement the three functions below:
# is_edge_sorted
# classify_by_angles
# classify_by_edges

# ----- YOUR CODE STARTS HERE -----

def is_edge_sorted(a,b,c):
  return bool(a<=b and b<=c)

def classify_by_edges(a,b,c):
  if a+b<=c:
    return print("invalid")
  elif a==b==c:
    return print("equilateral")
  elif a==b or a==c or b==c:
    return print("isosceles")
  else:
    return print("scalene")

def classify_by_angles(a,b,c):
  if a+b<=c:
    return print("invalid")
  if c**2 == a**2 + b**2:
    return print("right")
  if c**2 > a**2 + b**2:
    return print("obtuse")
  else:
    return print("acute")



# ===== YOUR CODE ENDS HERE =====


# This is utility function. Do NOT modify this function
def print_triangle_class(a, b, c, f):
  print(f'Triangle ({a}, {b}, {c}) is {"not edge sorted" if not is_edge_sorted(a, b, c) else f(a, b, c)}')


