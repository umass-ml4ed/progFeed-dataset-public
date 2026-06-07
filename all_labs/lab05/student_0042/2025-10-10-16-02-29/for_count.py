# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(a, n):
    count = 0
    for item in a:
        if len(item) >= n:
            count = count+1
        else:
            count = count #the code kept returning errors unless I put something here
    return count

print(count_strings(["", "a", "aa", "aaa"], 1.5))

#It also works with decimal values, 0.5 yields 3, I guess it's expected but still cool.