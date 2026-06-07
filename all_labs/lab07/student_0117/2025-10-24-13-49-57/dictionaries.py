# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_words(touple_insert):
    some_dict = {}
    for word in touple_insert:
        if word in some_dict:
            some_dict[word] += 1
        else:
            some_dict[word] = 1
    return some_dict

def average_prices(big_touple):
    final_dict = {}
    length_dict = {}
    sum_dict = {}
    for one_instance in big_touple:
        name = one_instance[0]
        price = one_instance[1]
        final_dict[name] = 0
        if name in length_dict:
            length_dict[name].append("1")
        else:
            length_dict[name] = ["1"]
        if name in sum_dict:
            sum_dict[name] += price
        else:
            sum_dict[name] = price
    for key in final_dict:
        final_dict[key] = (sum_dict[key])/(len(length_dict[key]))
    return final_dict

def count_bigrams(tuple_of_strings):
    some_dict = {}
    count = 0
    for word in tuple_of_strings[:-1]:
        if (word, tuple_of_strings[count + 1]) in some_dict:
            some_dict[(word, tuple_of_strings[count + 1])] += 1
        else:
            some_dict[(word, tuple_of_strings[count + 1])] = 1
        some_dict[(word, tuple_of_strings[count + 1])]
        count += 1
    return some_dict

