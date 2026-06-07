# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
def combine_lists(a,b):
    if b:
        a.insert(0,b[0])
        a.append(b[-1])
    if len(a)%2 != 0:
        middle_value = len(a)//2
        a.pop(middle_value)
    return a
print(combine_lists([1, 2, 3],[4, 5, 6, 7]))
