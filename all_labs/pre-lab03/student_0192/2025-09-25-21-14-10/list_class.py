# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED



def combine_lists(a,b):
    b1 = b[0]
    b2 = b[-1]
    a.insert(0,b1)
    a.append(b2)
    middle = len(a)//2
    a.pop(middle)
    return(a)

print(combine_lists([1, 2, 3],[4, 5, 6, 7]))
print(combine_lists([1, 2, 3, 4, 5],[4, 5, 6, 7]))

def classify_by_length(a):
    if list(a) == []:
        return("empty")
    elif len(a) % 2 == 0:
        return("even_length")
    else:
        return("odd_length")
   

print(classify_by_length([1, 2, 3]))
print(classify_by_length([1, 2, 2, 3]))
print(classify_by_length([]))


