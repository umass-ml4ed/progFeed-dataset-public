# Author  : REDACTED
# Email : REDACTED
# Spire ID  : REDACTED



# Implement the three functions below:
# is_edge_sorted
# classify_by_angles
# classify_by_edges

# ----- YOUR CODE STARTS HERE -----

import math 

def is_edge_sorted(a, b, c):
    return (a<=b<=c)

def classify_by_edges(a, b, c):
   if (a+b<=c):
      return "invalid"
   if (a==b==c):
      return "equilateral"
   if (a == b or b == c or a == c):
      return "isosceles"
   else:
      return "scalene"

def classify_by_angles(a, b, c):
   if (a<=0 or b<=0 or c<=0 or a+b<= c or a + c <= b or b + c <= a):
      return "invalid"
   sides = sorted([a, b, c])
   a, b, c = sides
   c_squared = c ** 2
   squares_sum = a ** 2 + b ** 2
   if abs(c_squared - squares_sum) < 1e-6:
        return "right"
   elif c_squared > squares_sum:
        return "obtuse"
   else:
        return "acute"

   #elif (c==90 or a==90 or b==90):
    #  return "right"
   #elif (c>=90 or a>=90 or b>=90):
    #  return "obtuse"
   #elif ( a < 90 and b < 90 and c < 90):
    #  return "acute"

# ===== YOUR CODE ENDS HERE =====


# This is utility function. Do NOT modify this function
def print_triangle_class(a, b, c, f):
  print(f'Triangle ({a}, {b}, {c}) is {"not edge sorted" if not is_edge_sorted(a, b, c) else f(a, b, c)}')

# You can use the code below to help test your functions

# Uncomment the following 5 lines (i.e. remove the starting # characters on each line) to test is_edge_sorted
#print(is_edge_sorted(3, 4, 5)) # should print True
#print(is_edge_sorted(3, 3, 3)) # should print True
#print(is_edge_sorted(3, 2, 4)) # should print False
#print(is_edge_sorted(2, 5, 3)) # should print False
#print(is_edge_sorted(3, 5, 3)) # should print False

# Uncomment the following 6 lines (i.e. remove the starting # characters on each line) to test classify_by_angles
print_triangle_class(3, 4, 7, classify_by_angles) # invalid
print_triangle_class(3, 4, 5, classify_by_angles) # right
print_triangle_class(3, 3, 3, classify_by_angles) # acute
print_triangle_class(2, 3, 4, classify_by_angles) # obtuse
print_triangle_class(4, 5, 6, classify_by_angles) # acute
print_triangle_class(5, 12, 13, classify_by_angles) # right

# Uncomment the following 6 lines (i.e. remove the starting # characters on each line) to test classify_by_edges
#print_triangle_class(3, 4, 8, classify_by_edges) # invalid
#print_triangle_class(3, 4, 5, classify_by_edges) # scalene
#print_triangle_class(3, 3, 3, classify_by_edges) # equilateral
#print_triangle_class(5, 5, 6, classify_by_edges) # isosceles
#print_triangle_class(5, 6, 6, classify_by_edges) # isosceles
#print_triangle_class(1, 2, 3, classify_by_edges) # invalid