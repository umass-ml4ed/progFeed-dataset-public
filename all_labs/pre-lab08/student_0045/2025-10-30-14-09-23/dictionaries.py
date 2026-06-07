# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def most_frequent_element(lst: list):
    if not lst:
        return None
    dct = {}
    for item in lst:
        dct[item] = dct.get(item, 0) + 1

    count = 0
    frequent = None
    for item, number in dct.items():
        if number>count:
            count = number
            frequent = item

    return frequent

print(most_frequent_element([3, 1, 3, 2, 3, 1, 2, 2, 2]))