# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(str_lst, n):
    cnt=0
    for str in str_lst:
        if(len(str)>=n):
            cnt+=1
    return cnt

print(count_strings(['', 'a', 'aa', 'aaa'], 0))   # should return 4
print(count_strings(['', 'a', 'aa', 'aaa'], 2))   # should return 2 
print(count_strings(['', 'a', 'aa', 'aaa'], 4))   # should return 0
