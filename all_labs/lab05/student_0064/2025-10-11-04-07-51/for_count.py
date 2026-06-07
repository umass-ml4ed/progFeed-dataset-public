# Author  : REDACTED
# Email : REDACTED
# Spire ID  : REDACTED
    
def count_strings(s_list, n):
    count = 0
    for string in s_list:
        if len(string) >= n:
            count += 1
    return count

print(count_strings(['', 'a', 'aa', 'aaa'], 0))
print(count_strings(['', 'a', 'aa', 'aaa'], 2))
print(count_strings(['', 'a', 'aa', 'aaa'], 4))

count_strings(['', 'a', 'aa', 'aaa'], 0)   # should return 4
count_strings(['', 'a', 'aa', 'aaa'], 2)   # should return 2 
count_strings(['', 'a', 'aa', 'aaa'], 4)   # should return 0

