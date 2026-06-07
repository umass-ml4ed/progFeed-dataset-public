# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

# Below, please implement the combine_lists() function as specified in the pre-lab instructions.
# ----- YOUR CODE STARTS HERE -----
def combine_lists(a, b):
    a.insert(0, b[0])
    a.append(b[-1])
    c= len(a) // 2
    a.remove(a[c])
    return(a)

def classify_by_length(a):
    if classify_by_length(len(0)):
        print("empty")
    elif classify_by_length((len//2)==1):
        print("odd_length")
    else:
        print("even_length")
# ===== YOUR CODE ENDS HERE =====

# You can use the code below to help test your functions

# Uncomment the following lines (remove the # characters on each line)
# to test combine_lists()
#print(combine_lists([1, 2, 3],[4, 5, 6, 7]))
#print(combine_lists([1, 2, 3, 4, 5],[4, 5, 6, 7]))

# Uncomment the following lines (remove the # characters on each line)
# to test classify_by_length()
print(classify_by_length([1, 2, 3]))
print(classify_by_length([1, 2, 2, 3]))
print(classify_by_length([]))