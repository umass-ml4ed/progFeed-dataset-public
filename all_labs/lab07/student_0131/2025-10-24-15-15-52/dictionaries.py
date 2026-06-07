def count_words(words):
    some_dict = {}
    for letters in words:
        if letters in some_dict:
            some_dict[letters]+=1
        else:
            some_dict[letters]=1
    return some_dict



words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
print(count_words(words))

