# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


# Below, please implement the combine_lists() function as specified in the pre-lab instructions.
# ----- YOUR CODE STARTS HERE -----
lst = []
b_lst = []
def combine_lists(lst, b_lst):
    lst.insert(0, b_lst[0])
    lst.append(b_lst[-1])
    m = len(lst) // 2
    del lst[m]
    return lst

def classify_by_length(lst):
    a = int(len(lst))
    if a == 0:
        print(lst)
        return "empty"
    if a % 2 == 0:
        print(lst)
        return "even_length"
    else:
        print(lst)
        return "odd_length"


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
