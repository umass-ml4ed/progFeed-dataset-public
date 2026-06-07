# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED



# Implement the three functions below:
# is_edge_sorted
# classify_by_angles
# classify_by_edges

# ----- YOUR CODE STARTS HERE -----
def is_edge_sorted (a, b ,c):
    if (a <= b <= c):
       return True
    else:
       return False

def classify_by_edges (a, b, c):
    if ((a+b)<=c):
        return ('invalid')
    else:
        if a== b== c:
           return ('equilateral')
        else:
            if a==b!=c or b==c!=a or a==c!=b:
             return ('isosceles')
            else:
             return ('scalene')  

def classify_by_angles (a, b ,c):
    if ((a+b)<=c):
       return ('invalid')
    else:
     if (a**2)+(b**2)==(c**2):
        return ('right')
     else:
       if (a**2)+(b**2)<(c**2):
          return ('obtuse')
       else:
          if (a**2)+(b**2)>(c**2):
            return ('acute')
          else:
             return ('invalid')
a = int(input("what is the first side of the triangle? "))
b = int(input("what is the second side of the triangle? "))
c = int(input("what is the third side of the triangle? "))

print(str(f"\nChecking if edges are sorted:"))
print(is_edge_sorted(a, b, c))

print(str(f"\nClassifying by edges:"))
print(classify_by_edges(a, b, c))

print(f"\nClassifying by angles:")
print((classify_by_angles(a, b, c)))
# ===== YOUR CODE ENDS HERE =====


# This is utility function. Do NOT modify this function
def print_triangle_class(a, b, c, f):
  print(f'Triangle ({a}, {b}, {c}) is {"not edge sorted" if not is_edge_sorted(a, b, c) else f(a, b, c)}')

# You can use the code below to help test your functions
