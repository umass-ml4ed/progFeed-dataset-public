# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_edge_sorted(a,b,c):
    if a <= b and b <= c:
        return True
    else:
        return False
print(is_edge_sorted(3, 4, 5))

print(is_edge_sorted(3, 5, 3))



    

    #Since we assume the three edges a, b, and c must be sorted, let’s first write a function to check whether this condition is True. Write a function, called is_edge_sorted, which should:
#Take the three edges a, b, c as parameters
#Return boolean True if a<=b and b<=c; otherwise, return boolean False

 