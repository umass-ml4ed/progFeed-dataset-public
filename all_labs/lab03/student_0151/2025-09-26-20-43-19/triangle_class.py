# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_edge_sorted(x,y,z):
  check = [x,y,z]
  if sorted(check) == check:
    return True
  else:
    return False
  

def classify_by_edges(a,b,c):
  if a+b<=c:
    if a == b and b == c and a == c:
      return "equilateral"
    elif a == b or b == c or a == c:
      return "isosceles"
    else:
      return "scalene"
  else:
    return "invalid"
  

def classify_by_angles(a,b,c):
  if a+b<=c:
    return "invalid"
  
  if a == 90 or b == 90 or c == 90:
    return "right"
  elif a < 90 and b < 90 and c < 90:
    return "acute"
  else:
    return "obtuse"

    


