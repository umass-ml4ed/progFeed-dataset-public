# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

# Below, please implement the combine_lists() function as specified in the pre-lab instructions.
# ----- YOUR CODE STARTS HERE -----

def combine_lists(l1,l2):
    l1.insert(0,l2[0])
    l1.append(l2[-1])
    l1.pop(int((len(l1)/2)))
    return l1

def classify_by_length(lst):
    if len(lst)==0:
        return "empty"
    elif len(lst)%2==1:
        return "odd_length"
    elif len(lst)%2==0:
        return "even_length"

# ===== YOUR CODE ENDS HERE =====

# You can use the code below to help test your functions

# Uncomment the following lines (remove the # characters on each line)
# to test combine_lists()
print(combine_lists([1, 2, 3],[4, 5, 6, 7]))
print(combine_lists([1, 2, 3, 4, 5],[4, 5, 6, 7]))

# Uncomment the following lines (remove the # characters on each line)
# to test classify_by_length()
print(classify_by_length([1, 2, 3]))
print(classify_by_length([1, 2, 2, 3]))
print(classify_by_length([]))

