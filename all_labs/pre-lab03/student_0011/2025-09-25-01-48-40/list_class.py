#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

# Below, please implement the combine_lists() function as specified in the pre-lab instructions.
# ----- YOUR CODE STARTS HERE -----
def combine_lists(a,b):
    ab = b[0]
    a.insert(0, ab)
    ba = b[-1]
    a.append(ba)
    mid = len(a)//2
    del a [mid]
    return a

# ===== YOUR CODE ENDS HERE =====

# You can use the code below to help test your functions

# Uncomment the following lines (remove the # characters on each line)
# to test combine_lists()
#print(combine_lists([1, 2, 3],[4, 5, 6, 7]))
#print(combine_lists([1, 2, 3, 4, 5],[4, 5, 6, 7]))

# Uncomment the following lines (remove the # characters on each line)
# to test classify_by_length()
#print(classify_by_length([1, 2, 3])
#print(classify_by_length([1, 2, 2, 3])
#print(classify_by_length([])
