# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED



# Implement the three functions below:
# is_edge_sorted
# classify_by_angles
# classify_by_edges

# ----- YOUR CODE STARTS HERE -----

#1. implement is_edge_sorted

def is_edge_sorted (a,b,c):
  return a <= b <= c

print(is_edge_sorted(3, 4, 5))
print(is_edge_sorted(3, 2, 4))

#2. implement classify_by_edges

def classify_by_edges (a,b,c):
  if (a + b <= c):
    return "invalid"
  elif (a == b == c):
    return "equilateral"
  elif (a == b or a == c or b == c):
    return "isosceles"
  else:
    return "scalene"
def triangle_class (x,y,z,classifir):
  a, b, c = sorted ([x,y,z])
  return classifir (a,b,c)
print (triangle_class(3, 4, 8, classify_by_edges)) # invalid
print(triangle_class(3, 4, 5, classify_by_edges)) # scalene
print(triangle_class(3, 3, 3, classify_by_edges)) # equilateral
print(triangle_class(5, 5, 6, classify_by_edges)) # isosceles
print(triangle_class(5, 6, 6, classify_by_edges)) # isosceles
print(triangle_class(1, 2, 3, classify_by_edges)) # invalid

#3. implement classify_by_angles

def classify_by_angles(a,b,c):
  sides = sorted ([a,b,c])
  a, b, c = sides[0], sides[1], sides[2]
  if (a+b <= c):
    return "invalid"
  
  if (c**2 == a**2 + b**2):
    return "right"
  elif (c**2 > a**2 + b**2):
    return "obtuse"
  else:
    return "acute"
def traingle_class (a,b,c,fuc):
  return fuc(a,b,c)

print(triangle_class(3, 4, 7, classify_by_angles)) # invalid
print(triangle_class(3, 4, 5, classify_by_angles)) # right
print(triangle_class(3, 3, 3, classify_by_angles)) # acute
print(triangle_class(2, 3, 4, classify_by_angles)) # obtuse
print(triangle_class(4, 5, 6, classify_by_angles)) # acute
print(triangle_class(5, 12, 13, classify_by_angles)) # right

# ===== YOUR CODE ENDS HERE =====


# This is utility function. Do NOT modify this function
#def print_triangle_class(a, b, c, f):
  #print(f'Triangle ({a}, {b}, {c}) is {"not edge sorted" if not is_edge_sorted(a, b, c) else f(a, b, c)}')

# You can use the code below to help test your functions

# Uncomment the following 5 lines (i.e. remove the starting # characters on each line) to test is_edge_sorted
# print(is_edge_sorted(3, 4, 5)) # should print True
# print(is_edge_sorted(3, 3, 3)) # should print True
# print(is_edge_sorted(3, 2, 4)) # should print False
# print(is_edge_sorted(2, 5, 3)) # should print False
# print(is_edge_sorted(3, 5, 3)) # should print False

# Uncomment the following 6 lines (i.e. remove the starting # characters on each line) to test classify_by_angles
# print_triangle_class(3, 4, 7, classify_by_angles) # invalid
# print_triangle_class(3, 4, 5, classify_by_angles) # right
# print_triangle_class(3, 3, 3, classify_by_angles) # acute
# print_triangle_class(2, 3, 4, classify_by_angles) # obtuse
# print_triangle_class(4, 5, 6, classify_by_angles) # acute
# print_triangle_class(5, 12, 13, classify_by_angles) # right

# Uncomment the following 6 lines (i.e. remove the starting # characters on each line) to test classify_by_edges
# print_triangle_class(3, 4, 8, classify_by_edges) # invalid
# print_triangle_class(3, 4, 5, classify_by_edges) # scalene
# print_triangle_class(3, 3, 3, classify_by_edges) # equilateral
# print_triangle_class(5, 5, 6, classify_by_edges) # isosceles
# print_triangle_class(5, 6, 6, classify_by_edges) # isosceles
# print_triangle_class(1, 2, 3, classify_by_edges) # invalid