# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

# Below, please implement the combine_lists() function as specified in the pre-lab instructions.
# ----- YOUR CODE STARTS HERE -----
def combine_lists(a, b):
    a_length = len(a)
    b_length = len(b)
    if a_length % 2 == 0:
        if a_length == 0 or b_length == 0:
            return a
        return a
    else:
        b_first = b.pop(0)
        a.insert(0, b_first)
        b_last = b.pop(-1)
        a.append(b_last)
        a_mid = len(a) // 2
        a.pop(a_mid)
        return a

def classify_by_length(a):
    length = len(a)
    if length == 0:
        return "empty"
    elif length % 2 == 0:
        return "even_length"
    else:
        return "odd_length"
    
# ===== YOUR CODE ENDS HERE =====

# You can use the code below to help test your functions

# Uncomment the following lines (remove the # characters on each line)
# to test combine_lists()
print(combine_lists([1, 2, 3],[4, 5, 6, 7]))
print(combine_lists([1, 2, 3, 4, 5],[4, 5, 6, 7]))
print(combine_lists([], []))

# Uncomment the following lines (remove the # characters on each line)
# to test classify_by_length()
#print(classify_by_length([1, 2, 3]))
#print(classify_by_length([1, 2, 2, 3]))
#print(classify_by_length([]))
