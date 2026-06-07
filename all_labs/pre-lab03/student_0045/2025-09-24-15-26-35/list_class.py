# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
def combine_lists(a,b):
    if b:
        a.insert(0,b[0])
        a.append(b[-1])
        middle_value = len(a)//2
        a.pop(middle_value)
    return a
print(combine_lists([1, 2, 3],[4, 5, 6, 7]))


def classify_by_length(a):
    if len(a)==0:
        return 'empty'
    elif len(a)%2==0:
        return 'even_length'
    else:
        return 'odd_length'
print(classify_by_length([1, 2, 3]))
