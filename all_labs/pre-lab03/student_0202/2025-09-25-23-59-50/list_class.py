# AUTHOR   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


# Below, please implement the combine_lists() function as specified in the pre-lab instructions.
# ----- YOUR CODE STARTS HERE -----

def combine_lists(a: list, b: list) -> list:
    """
    Takes the two lists a and b as parameters. 
    Inserts the first element of b at the beginning of a.
    Inserts the last element of b at the end of a.
    Deletes the middle element of a.
    Returns the resultant list a after all the changes. 
    """
    a.insert(b[0],0)
    a.insert(b[-1],-1)
    a.pop((len(a)+1)/2)

    return a

def classify_by_length(a: list) -> str:
    """
    Takes one list of integers, a as the parameter.
    Returns a string representing the list class. The string must be one of empty, 
    odd_length, or even_length, and it may NOT be anything else. 
    Returns empty if the list is empty.
    Returns odd_length if the list has an odd length.
    Returns even_length if the list has an even length.
    """
    lst = ["empty","even_length","odd_length"]

    if len(a) == 0:
        result = lst[0]
    elif len(a) % 2 == 0:
        result = lst[1]
    else:
        result = lst[2]   

    return result

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
