# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def most_frequent_element(lst):
    dict = {}
    maximum = 0
    if len(lst) > 0:
        for element in lst:
            if element in dict:
                dict[element] = dict[element] + 1
            else:
                dict[element] = 1
        maximum = max(dict.values())
        for key in dict:
            if dict[key] == maximum:
                return key
    else:
        return None
print(most_frequent_element([]))
