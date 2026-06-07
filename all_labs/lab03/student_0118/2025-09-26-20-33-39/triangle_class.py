# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

#is_edge_sorted
def is_edge_sorted(a, b, c):
  if a <= b and b <= c:
    return True
  else: 
    return False
    
#classify_by_edges

def classify_by_edges(a, b, c):
  if a + b <= c:
    return str("invalid")
  elif a == b == c:
    return str("equilateral")
  elif a == b or a == c or b == c:
    return str("isosceles")
  else:
    return str("scalene")

#classify_by_angles

def classify_by_angles(a, b, c):
  if a + b <= c:
    return str("invalid")
  elif (a**2 + b**2) == c**2: 
    return str("right")
  elif (a**2 + b**2) < c**2:
    return str("obtuse")
  else:
    return str("acute")





#print(is_edge_sorted(3, 4, 5)) # should print True
#print(is_edge_sorted(3, 3, 3)) # should print True
#print(is_edge_sorted(3, 2, 4)) # should print False
#print(is_edge_sorted(2, 5, 3)) # should print False
#print(is_edge_sorted(3, 5, 3)) # should print False


print(classify_by_angles(3, 4, 7)) # invalid
print(classify_by_angles(3, 4, 5)) # right
print(classify_by_angles(3, 3, 3)) # acute
print(classify_by_angles(2, 3, 4)) # obtuse
print(classify_by_angles(4, 5, 6)) 
print(classify_by_angles(5, 12, 13)) 


#print(classify_by_edges(3, 4, 8)) # invalid
#print(classify_by_edges(3, 4, 5)) # scalene
#print(classify_by_edges(3, 3, 3)) # equilateral
#print(classify_by_edges(5, 5, 6)) # isosceles
#print(classify_by_edges(5, 6, 6)) # isosceles
#print(classify_by_edges(1, 2, 3)) #invalid