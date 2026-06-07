# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    """
    Returns the maximum element of a list of integers using recursion only.
    """
    # Base Case: If the list is empty, return 0 (as per example)
    if not lst:
        return 0
    
    # Base Case: If the list has only one item, that item is the max
    if len(lst) == 1:
        return lst[0]
    
    # Recursive Step: 
    # Get the max of the rest of the list
    max_of_rest = max_recursive(lst[1:])
    
    # Compare the first item to the max of the rest
    if lst[0] > max_of_rest:
        return lst[0]
    else:
        return max_of_rest


def sum_lists_recursive(lst1, lst2):
    """
    Returns the summation of the elements of two input lists of equal length.
    """
    # Base Case: If the lists are empty, the sum is 0
    if not lst1:
        return 0
    
    # Recursive Step:
    # Add the first elements of both lists, plus the recursive sum of the rest
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])


def funky(n):
    """
    Implements the recursive function f(n) defined in the lab image.
    """
    # Base Case: if n is 0 or 1
    if n == 0 or n == 1:
        return 1
    
    # Recursive Case: if n is an even number
    elif n % 2 == 0:
        return 2 * funky(n // 2)
    
    # Recursive Case: otherwise (n is odd and not 1)
    else:
        return 1 + 2 * funky(n + 1)


def permutations(lis):
    """
    Returns a list of all permutations of the input list.
    """
    # Base Case: if lis has only 1 item, return [lis]
    if len(lis) == 1:
        return [lis]
    
    retlis = []
    
    # Loop over the index range of lis
    for i in range(len(lis)):
        # Assign the current item to front_item
        front_item = lis[i]
        
        # Make a new list containing remaining items (slicing)
        remaining = lis[:i] + lis[i+1:]
        
        # Recursive step: get permutations of the remaining items
        perms_of_remaining = permutations(remaining)
        
        # Loop over the returned permutations and insert front_item
        for p in perms_of_remaining:
            # Create the new permutation
            new_perm = [front_item] + p
            # Append to result list
            retlis.append(new_perm)
            
    return retlis

# --- Test Cases to Verify Implementation ---
if __name__ == "__main__":
    print("--- Testing max_recursive ---")
    print(f"max_recursive([3, 10, 2, 8, 6]) -> {max_recursive([3, 10, 2, 8, 6])}") # Expected: 10
    print(f"max_recursive([]) -> {max_recursive([])}") # Expected: 0

    print("\n--- Testing sum_lists_recursive ---")
    print(f"sum_lists_recursive([1, 2, 3], [4, 5, 6]) -> {sum_lists_recursive([1, 2, 3], [4, 5, 6])}") # Expected: 21
    
    print("\n--- Testing funky ---")
    print(f"funky(2)   -> {funky(2)}")   # Expected: 2
    print(f"funky(10)  -> {funky(10)}")  # Expected: 74
    print(f"funky(-10) -> {funky(-10)}") # Expected: 50
    print(f"funky(-50) -> {funky(-50)}") # Expected: 418

    print("\n--- Testing permutations ---")
    print(f"permutations(['AA', 'BB']) -> {permutations(['AA', 'BB'])}")