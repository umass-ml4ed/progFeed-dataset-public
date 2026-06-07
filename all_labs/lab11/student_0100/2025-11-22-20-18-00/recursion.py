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
    if n == 0:
        return 2
    elif n == 1:
        return 3
    
    # Recursive cases
    if n > 1:
        return 2 * funky(n - 1) - 3 * funky(n - 2)
    else:  # n < 0
        return 2 * funky(n + 2) - funky(n + 1)

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

# Test code (you can add this to verify your functions)
if __name__ == "__main__":
    # Test max_recursive
    print("Testing max_recursive:")
    print(max_recursive([3, 10, 2, 8, 6]))  # Should return 10
    print(max_recursive([10, 2, 8, 6]))     # Should return 10
    print(max_recursive([2, 8, 6]))         # Should return 8
    print(max_recursive([8, 6]))            # Should return 8
    print(max_recursive([6]))               # Should return 6
    print(max_recursive([]))                # Should return 0
    
    print("\nTesting sum_lists_recursive:")
    # Test sum_lists_recursive
    print(sum_lists_recursive([1, 2, 3], [4, 5, 6]))  # Should return 21
    print(sum_lists_recursive([2, 3], [5, 6]))        # Should return 16
    print(sum_lists_recursive([3], [6]))              # Should return 9
    print(sum_lists_recursive([], []))                # Should return 0
    
    print("\nTesting funky:")
    # Test funky
    print(funky(2))   # Should return 2
    print(funky(10))  # Should return 74
    print(funky(50))  # Should return 554
    print(funky(-10)) # Should return 50
    print(funky(-50)) # Should return 418
    
    print("\nTesting permutations:")
    # Test permutations
    print(permutations(['AA']))
    print(permutations(['AA', 'BB']))
    print(permutations(['AA', 'BB', 'CC']))