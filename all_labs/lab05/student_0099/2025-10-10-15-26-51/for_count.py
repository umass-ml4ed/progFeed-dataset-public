# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(string_list, n):
    """
    Counts how many strings in a list contain at least n characters.

    Args:
        string_list (list): A list of strings.
        n (int): The minimum number of characters required.

    Returns:
        int: The count of strings with at least n characters.
    """
    count = 0
    for s in string_list:
        if len(s) >= n:
            count += 1
    return count

print(f"Test 1: {count_strings(['', 'a', 'aa', 'aaa'], 0)}")   
print(f"Test 2: {count_strings(['', 'a', 'aa', 'aaa'], 2)}")   
print(f"Test 3: {count_strings(['', 'a', 'aa', 'aaa'], 4)}")   
print(f"Test 4: {count_strings(['hello', 'world', 'python'], 5)}") 
print(f"Test 5: {count_strings([], 3)}")                       
print(f"Test 6: {count_strings(['short', 'medium', 'long_string'], 6)}") 
