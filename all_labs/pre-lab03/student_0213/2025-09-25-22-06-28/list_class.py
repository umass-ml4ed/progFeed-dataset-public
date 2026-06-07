# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def combine_lists(a, b):
    bitem1 = b[0]
    a.insert(0, bitem1)
    n = len(b)
    blastitem = b[n-1]
    a.append(blastitem)
    n2 = len(a)
    a.pop(int(n2/2-0.5))
    return a

print(combine_lists([1, 2, 3], [4, 5, 6, 7]))
print(combine_lists([1, 2, 3, 4, 5], [4, 5, 6, 7]))

def classify_by_length(a):
    lengthy = len(a)
    if lengthy % 2 == 0 and lengthy != 0:
        return "even_length"
    if lengthy % 2 == 1:
        return "odd_length"
    if lengthy == 0:
        return "empty"
    
print(classify_by_length([1, 2, 3]))
print(classify_by_length([1, 2, 2, 3]))
print(classify_by_length([]))