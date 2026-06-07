# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(words):
    diction = {} 
    for n in words:
        if n not in diction:
            diction[n] = 1
        else:
            diction[n] += 1
    return diction

result = count_words(("apple", "banana", "apple", "orange", "banana", "apple"))
print(result)