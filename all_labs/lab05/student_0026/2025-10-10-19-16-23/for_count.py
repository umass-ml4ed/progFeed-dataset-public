# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(lst, n):
    ncharacters=0
    for string in lst:
        if len(string)>=n:
            ncharacters+=1
        else:
            ncharacters=ncharacters
    return ncharacters

print(count_strings(['', 'a', 'aa', 'aaa'], 0))
print(count_strings(['', 'a', 'aa', 'aaa'], 2))
print(count_strings(['', 'a', 'aa', 'aaa'], 4))

