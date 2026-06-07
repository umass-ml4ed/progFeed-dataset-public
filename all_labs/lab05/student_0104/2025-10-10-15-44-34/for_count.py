# Author    : REDACTED
# Email     : REDACTED
# Spire ID  : REDACTED

def count_strings(strings, n: int):
    
    number = 0
    
    for i in strings:
        
        if len(i) >= n:
            
            number += 1
            
    return number

# print(count_strings(['', 'a', 'aa', 'aaa'], 0))   # should return 4
# print(count_strings(['', 'a', 'aa', 'aaa'], 2))   # should return 2 
# print(count_strings(['', 'a', 'aa', 'aaa'], 4))   # should return 0
