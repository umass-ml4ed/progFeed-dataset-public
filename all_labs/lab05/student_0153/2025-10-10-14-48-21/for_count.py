# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def count_strings(str_list, num):
    count = 0
    for s in str_list:
        if len(s) >= num:
            count += 1
    return count
print(count_strings(['', 'a', 'aa', 'aaa'], 0))
print(count_strings(['', 'a', 'aa', 'aaa'], 2))  
print(count_strings(['', 'a', 'aa', 'aaa'], 4))