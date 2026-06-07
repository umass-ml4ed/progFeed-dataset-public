#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def count_strings(list_of_strings: list, n: int) -> int:
    count = 0
    for string in list_of_strings:
        if len(string) >= n:
            count +=1
    return count


