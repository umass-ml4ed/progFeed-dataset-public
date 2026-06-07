# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED


def count_words(tow: tuple) -> dict:

    some_dict = {}

    for s in tow:

        if s in some_dict:

            some_dict[s] += 1

        else:

            some_dict[s] = 1
        
    return some_dict


def average_prices(top: tuple) -> dict:

    some_dict = {}

    for t in top:

        sum = 0

        count = 0

        for i in range(len(top)):
            
            if t[0] == top[i][0]:
                
                sum += top[i][1]

                count += 1
        
        avg = sum / count

        some_dict[t[0]] = avg

    return some_dict


def count_bigrams(tow: tuple) -> dict:

    some_dict = {}

    for i in range(len(tow) - 1):

        bigram = (tow[i],tow[i+1])

        if bigram in some_dict:

            some_dict[bigram] += 1
        
        else:

            some_dict[bigram] = 1

    return some_dict

