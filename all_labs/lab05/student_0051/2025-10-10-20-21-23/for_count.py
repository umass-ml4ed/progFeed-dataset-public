# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(str_list, n):
    count = 0 
    for string in str_list: 
        if len(string) >= n: 
            count += 1
    return count 

count_strings(['', 'a', 'aa', 'aaa'], 0)
count_strings(['', 'a', 'aa', 'aaa'], 2) 
count_strings(['', 'a', 'aa', 'aaa'], 4)
