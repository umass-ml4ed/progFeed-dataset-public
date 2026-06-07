# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

# 1. Implement function max_recursive
def max_recursive(lst):
    """
    Returns the maximum element of a list of integers using recursion.
    """
    # Base cases
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    
    # Recursive case: compare first element with max of the rest
    max_of_rest = max_recursive(lst[1:])
    return lst[0] if lst[0] > max_of_rest else max_of_rest

# 2. Implement function sum_lists_recursive
def sum_lists_recursive(lst1, lst2):
    """
    Returns the summation of elements from two lists of equal length using recursion.
    """
    # Base case: both lists are empty
    if len(lst1) == 0 and len(lst2) == 0:
        return 0
    
    # Recursive case: sum first elements and recurse on the rest
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])

# 3. Implement function funky
def funky(n):
    """
    Implements the recursive funky function as defined in the problem.
    """
    # Base cases
    if n == 0 or n == 1:
        return 1
    
    # Recursive cases
    if n % 2 == 0:  # n is even
        return 2 * funky(n // 2)
    else:  # n is odd
        return 1 + 2 * funky(n + 1)

# 4. Implement function permutations (Optional)
def permutations(lis):
    """
    Returns all possible permutations of the input list using recursion.
    """
    # Base case: list with only 1 element
    if len(lis) == 1:
        return [lis]
    
    retlis = []  # List to store all permutations
    
    # Loop through each element to use as the front item
    for i in range(len(lis)):
        front_item = lis[i]
        
        # Create list of remaining items (all except current front_item)
        remaining = lis[:i] + lis[i+1:]
        
        # Recursively get permutations of remaining items
        perms_of_remaining = permutations(remaining)
        
        # Add front_item to the beginning of each permutation
        for perm in perms_of_remaining:
            retlis.append([front_item] + perm)
    
    return retlis

# Test code
if __name__ == "__main__":
    # Test funky with the given examples
    print("Testing funky:")
    print(f"funky(0) = {funky(0)}")   # Should return 1
    print(f"funky(1) = {funky(1)}")   # Should return 1
    print(f"funky(2) = {funky(2)}")   # Should return 2*f(1) = 2*1 = 2
    print(f"funky(10) = {funky(10)}") # Let's trace this
    
    # Let's trace funky(10):
    # f(10) = 2*f(5)  (since 10 is even)
    # f(5) = 1 + 2*f(6)  (since 5 is odd)
    # f(6) = 2*f(3)  (since 6 is even)  
    # f(3) = 1 + 2*f(4)  (since 3 is odd)
    # f(4) = 2*f(2)  (since 4 is even)
    # f(2) = 2*f(1) = 2*1 = 2
    # So: f(4) = 2*2 = 4
    # f(3) = 1 + 2*4 = 9
    # f(6) = 2*9 = 18
    # f(5) = 1 + 2*18 = 37
    # f(10) = 2*37 = 74 ✓