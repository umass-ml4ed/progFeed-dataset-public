# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def count_strings(l: list, n: int) -> int:
    '''This function will return how many strings in the list that have at
    least n characters, and input n should be a natural number.'''
    argument = ''
    condition = True
    while condition == True:
        if type(n) != 'int' or n < 0:
            argument += '\n The input of \'n\' is not valid.'
        if type(l) == 'list':   
            if len(l) == 0:
                argument += '\'l\' should have some element.'
            else:
                for ele in l:
                    if type(ele) != 'string':
                        argument += 'The input of \'l\' is not valid.'
        else:
            argument += 'The input of \'l\' is not a list.'
    
    count = 0
    for str in l:
        if len(str) >= n:
            count += 1
    return count


print(count_strings(['', 'a', 'aa', 'aaa'], 0)) 
print(count_strings(['', 'a', 'aa', 'aaa'], 2))   
print(count_strings(['', 'a', 'aa', 'aaa'], 4))
print(count_strings(['', 'a', 'aa', 'aaa'], 0)) 
print(count_strings(['', 'a', 'aa', 'aaa'], 2))   
print(count_strings(['', 'a', 'aa', 'aaa'], 'xx'))