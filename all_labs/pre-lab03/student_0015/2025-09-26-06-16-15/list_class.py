# Author: REDACTED
# Email: REDACTED
# SPIRE ID: REDACTED

# Function 1: combine_lists
def combine_lists(a, b):
    # Insert first element of b at beginning of a
    a.insert(0, b[0])
    
    # Insert last element of b at the end of a
    a.append(b[-1])
    
    # Delete the middle element of a (since a had odd length before deletion)
    middle_index = len(a) // 2
    del a[middle_index]
    
    return a


# Function 2: classify_by_length
def classify_by_length(a):
    if len(a) == 0:
        return "empty"
    elif len(a) % 2 == 0:
        return "even_length"
    else:
        return "odd_length"


# --------------------------
# Example Test Runs
# --------------------------

# Test combine_lists
''' list_a = [1, 2, 3, 4, 5]
list_b = [10, 20, 30]
print(combine_lists(list_a, list_b))  
# Expected: [10, 1, 2, 4, 5, 30]

# Test classify_by_length
print(classify_by_length([1, 2, 3]))       # odd_length
print(classify_by_length([1, 2, 2, 3]))    # even_length
print(classify_by_length([]))              # empty '''

    