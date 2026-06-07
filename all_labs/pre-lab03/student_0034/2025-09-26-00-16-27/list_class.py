# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


# Below, please implement the combine_lists() function as specified in the pre-lab instructions.
# ----- YOUR CODE STARTS HERE -----
def combine_lists(a,b):
    a.insert(0, b[0])
    a.insert(-1, b[-1])
    a.pop(len(a)//2)
    return a

def classify_by_length(a):
    if len(a) == 0:
        return print("empty")
    elif len(a) % 2 == 0:
        return print("even_length")
    else: return print("odd_length")
# ===== YOUR CODE ENDS HERE =====

# You can use the code below to help test your functions

 #Uncomment the following lines (remove the characters on each line)
 #to test combine_lists()
#print(combine_lists([1, 2, 3],[4, 5, 6, 7]))
#print(combine_lists([1, 2, 3, 4, 5],[4, 5, 6, 7]))

# Uncomment the following lines (remove the # characters on each line)
# to test classify_by_length()
print(classify_by_length([1, 2, 3]))
print(classify_by_length([1, 2, 2, 3]))
print(classify_by_length([]))
