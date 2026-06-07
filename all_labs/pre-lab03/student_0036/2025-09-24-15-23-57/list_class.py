# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


# Below, please implement the combine_lists() function as specified in the pre-lab instructions.
# ----- YOUR CODE STARTS HERE -----
def combine_lists(a: list,b: list):
    a.insert(0,b[0])
    a.insert(len(a),b[len(b)-1])
    a.pop(len(a)//2)
    return a

def classify_by_length(a:list):
   d="empty"
   b="odd_length"
   c="even_length"
   if len(a)==0:
        return d
   elif len(a)%2!=1:
        return c
   else:
        return b


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

