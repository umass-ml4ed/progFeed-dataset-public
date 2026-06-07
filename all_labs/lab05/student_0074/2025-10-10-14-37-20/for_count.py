# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_strings(lis, n):
    k = 0
    for i in lis:           
        if len(i) >= n:     
            k += 1
    return k
#print(count_strings(['', 'a', 'aa', 'aaa'], 0)) 
#print(count_strings(['', 'a', 'aa', 'aaa'], 2))  
#print(count_strings(['', 'a', 'aa', 'aaa'], 4))
