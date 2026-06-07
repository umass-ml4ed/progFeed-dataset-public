# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def classify_by_length(a):
    if len(a) == 0:
        return "empty"
    elif len(a) % 2 == 1:
        return "odd_length"
    else:
        return "even_length"
print(classify_by_length([1, 2, 3]))
print(classify_by_length([1, 2, 2, 3]))
print(classify_by_length([]))