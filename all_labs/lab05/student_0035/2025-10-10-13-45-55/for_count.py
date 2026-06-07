# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

def count_strings(my_list, n):
    count = 0
    for i in my_list:
        if(len(i) >= n):
            count = count + 1
        else:
            continue
    
    return count

print(count_strings(['', 'a', 'as', 'aaa'], 0))
print(count_strings(['', 'a', 'as', 'aaa'], 4))
print(count_strings(['', 'a', 'as', 'aaa'], 2))