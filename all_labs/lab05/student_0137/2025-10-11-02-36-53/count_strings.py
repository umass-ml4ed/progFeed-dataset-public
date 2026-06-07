# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(lst, n):
    count = 0  # initialize counter
    for string in lst:      # loop over each string in the list
        if len(string) >= n:  # check if string length is at least n
            count += 1
    return count


# Example test cases (you can comment these out when submitting)
print(count_strings(['', 'a', 'aa', 'aaa'], 0))  
print(count_strings(['', 'a', 'aa', 'aaa'], 2))  
print(count_strings(['', 'a', 'aa', 'aaa'], 4))  