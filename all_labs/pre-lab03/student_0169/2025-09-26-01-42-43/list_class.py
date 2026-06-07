# AUTHOR   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


# ----- YOUR CODE STARTS HERE -----

def combine_lists(a, b):
    """
    Takes two lists a and b (of integers), and:
    - Inserts the first element of b at the beginning of a
    - Inserts the last element of b at the end of a
    - Deletes the middle element of a (assume a has odd length before deletion)
    - Returns the modified list
    """
    if not b:  
        return a

   
    a.insert(0, b[0])

   
    a.append(b[-1])

   
    mid_index = len(a) // 2
    del a[mid_index]

    return a


def classify_by_length(a):
    """
    Takes a list a of integers and returns:
    - "empty" if list is empty
    - "odd_length" if list has odd length
    - "even_length" if list has even length
    """
    if len(a) == 0:
        return "empty"
    elif len(a) % 2 == 0:
        return "even_length"
    else:
        return "odd_length"

# ===== YOUR CODE ENDS HERE =====


# You can use the code below to help test your functions

# Uncomment the following lines (remove the # characters on each line)
# to test combine_lists()
#print(combine_lists([1, 2, 3],[4, 5, 6, 7]))        # [4, 1, 3, 7]
#print(combine_lists([1, 2, 3, 4, 5],[4, 5, 6, 7]))  # [4, 1, 2, 4, 5, 7]

# Uncomment the following lines (remove the # characters on each line)
# to test classify_by_length()
#print(classify_by_length([1, 2, 3]))        # odd_length
#print(classify_by_length([1, 2, 2, 3]))     # even_length
#print(classify_by_length([]))               # empty
