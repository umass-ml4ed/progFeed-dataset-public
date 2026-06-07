#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def filter_positive(list_of_integers: list) -> list:
    only_pos = []
    for integer in list_of_integers:
        if integer > 0:
            only_pos.append(integer)
    return only_pos

print(filter_positive([1, -3, 5, 0, -2, 7]))
# [1, 5, 7]

print(filter_positive([-5, -1, -10]))
# []

print(filter_positive([10, 20, -30, 40]))
# [10, 20, 40]
