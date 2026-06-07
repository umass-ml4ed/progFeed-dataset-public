# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(string_lst, n: int):
    count = 0
    for i in range(len(string_lst)):
        string = string_lst[i]
        if len(string) >= n:
            count += 1
    return count



print(count_strings(['', 'a', 'aa', 'aaa'], 0))   # should return 4
print(count_strings(['', 'a', 'aa', 'aaa'], 2))  # should return 2
print(count_strings(['', 'a', 'aa', 'aaa'], 4))   # should return 0



