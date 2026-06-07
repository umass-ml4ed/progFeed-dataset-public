# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
import math

def is_edge_sorted(x,y,z):
  check = [x,y,z]
  if sorted(check) == check:
    return True
  else:
    return False
  

def classify_by_edges(a,b,c):
  if a+b<=c:
    return "invalid"
  if a == b and b == c and a == c:
    return "equilateral"
  elif a == b or b == c or a == c:
    return "isosceles"
  else:
    return "scalene"
  

def classify_by_angles(a,b,c):
  if a+b<=c:
    return "invalid"
  
  if a**2 + b**2 == c**2:
    return "right"
  elif a**2 + b**2 > c**2:
    return "acute"
  else:
    return "obtuse"
  

    


