# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
def count_words(words):
    result = {}
    for word in words:
        if word in result:
            result[word]+=1
        elif word not in result:
            result[word] = 1
    return result

words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))