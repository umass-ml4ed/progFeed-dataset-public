#Author : REDACTED
#Email : REDACTED
#Spire ID : REDACTED

def is_edge_sorted(a,b,c):
    return c >= b >= a
print (is_edge_sorted(1,2,3))

def classify_by_edges(a,b,c):
    if(a + b <= c):
        return "invalid"
    elif(a != b and b != c):
        return "scalene"
    elif(a == b and b == c):
        return "equilateral"
    else:
        return "isosceles"

print(classify_by_edges(4,4,4)) 

def classify_by_angles(a,b,c):
    if(a + b <= c):
        return "invalid"
    elif((c ** 2) > (a ** 2) + (b ** 2) ):
        return "Obtuse"
    elif((c ** 2) == (a ** 2) + (b ** 2)):
        return "right"
    else:
        return "acute"

print(classify_by_angles(3,4,5))