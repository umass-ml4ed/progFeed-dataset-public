# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

import math

# --- 1. Implement function max_recursive ---
def max_recursive(lst):
    """
    Returns the maximum element of a list of integers using recursion only.
    Returns 0 if the list is empty (base case).
    """
    # Base Case 1: Empty list (returns the default value as specified in the example)
    if not lst:
        return 0
    
    # Base Case 2: List with one element
    if len(lst) == 1:
        return lst[0]
    
    # Recursive Step: Compare the first element to the maximum of the rest of the list.
    
    # max_of_rest is the result of the recursive call on the rest of the list
    max_of_rest = max_recursive(lst[1:])
    
    # Comparison: Return the larger of the first element (lst[0]) or the max of the rest
    if lst[0] > max_of_rest:
        return lst[0]
    else:
        return max_of_rest

# --- 2. Implement function sum_lists_recursive ---
def sum_lists_recursive(lst1, lst2):
    """
    Takes two lists of integers of equal length and returns the summation of all
    elements combined, using recursion only.
    """
    # Base Case: When both lists are empty (since they have equal length)
    if not lst1:
        return 0
    
    # Recursive Step: Add the first elements from both lists, then recursively
    # call the function on the remainder of the lists (using slicing).
    
    current_sum = lst1[0] + lst2[0]
    
    # Recursively add the sum of the remaining elements
    return current_sum + sum_lists_recursive(lst1[1:], lst2[1:])

# --- 3. Implement function funky ---
def funky(n):
    """
    Implements the recursive mathematical function described in the problem.
    """
    # Base Case 1: n = 0
    if n == 0:
        return 1
    
    # Base Case 2: n = 1
    if n == 1:
        return 2
    
    # Case A: n > 1
    if n > 1:
        # Recursive Step: funky(n-1) + funky(n-2)
        return funky(n - 1) + funky(n - 2)
    
    # Case B: n < 0
    # Use n = n + 2 to progress towards the base cases (n=0 or n=1)
    if n < 0:
        # Recursive Step: 1 + funky(n + 2) + funky(n + 3)
        return 1 + funky(n + 2) + funky(n + 3)

# --- 4. Implement function permutations (Optional) ---
def permutations(lis):
    """
    Computes all possible permutations of the items in the input list.
    Returns a list of lists.
    """
    # Base Case: If the list has only 1 item, return that item as a list inside a list.
    if len(lis) == 1:
        return [lis]
    
    retlis = []  # Initialize the list to store all final permutations
    
    # Loop over the index to select each item as the 'front_item'
    for i in range(len(lis)):
        front_item = lis[i]
        
        # Create the list of remaining items (all items except lis[i])
        # Using slicing and list concatenation for clarity:
        remaining = lis[:i] + lis[i+1:] 
        
        # Recursive Step: Get all permutations of the remaining items
        # perm_of_rest will be a list of lists (e.g., [['B', 'C'], ['C', 'B']])
        perm_of_rest = permutations(remaining)
        
        # Combine the front_item with each permutation from the recursive call
        for p in perm_of_rest:
            # Create a new permutation by putting front_item at the beginning
            new_permutation = [front_item] + p
            retlis.append(new_permutation)
            
    return retlis