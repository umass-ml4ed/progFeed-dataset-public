#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def count_strings(lst, n):
    total = 0
    i = 0
    for i in range(len(lst)):
        str = lst[i]
        if len(str) >= n:
            total += 1
    return total 

print(count_strings(['', 'a', 'aa', 'aaa'], 0))   # should return 4
print(count_strings(['', 'a', 'aa', 'aaa'], 2))   # should return 2 
print(count_strings(['', 'a', 'aa', 'aaa'], 4))   # should return 0



            
