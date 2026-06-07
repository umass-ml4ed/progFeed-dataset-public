# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_strings(lst, n):
    new = []
    count = 0
    for characters in lst: 
        new.append(len(characters))
    for i in range(len(new)):
        if n <= new[i]:
            count = count + 1
            i+=1
    return count 




print(count_strings(['', 'a', 'aa', 'aaa'], 0) )  # should return 4
print(count_strings(['', 'a', 'aa', 'aaa'], 2))   # should return 2 
print(count_strings(['', 'a', 'aa', 'aaa'], 4))   # should return 0

