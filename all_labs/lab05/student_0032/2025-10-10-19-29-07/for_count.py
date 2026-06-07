# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def count_strings(list: list, n: int): 
    big_boss = 0
    for string in list: 
        if len(string) >= n: 
            big_boss += 1
    return big_boss

print(count_strings(['', 'a', 'aa', 'aaa'], 0)   )
print(count_strings(['', 'a', 'aa', 'aaa'], 2)   ) 
print(count_strings(['', 'a', 'aa', 'aaa'], 4)   )
