# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
def count_words(word_tuple):
    frequency_dict=dict()
    i=0
    for word in words:
        if word in words and word in frequency_dict:
            frequency_dict.update({word:i+1})
            i=i+1
        if word in words and word not in frequency_dict:
            frequency_dict.update({word:1})
    return frequency_dict

print(count_words(words))


