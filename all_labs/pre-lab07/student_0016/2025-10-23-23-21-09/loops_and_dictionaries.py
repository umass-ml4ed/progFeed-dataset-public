# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    stringy_thingy = ""
    while n > 0:
        for number in range(n, 1, -1):
            stringy_thingy += str(number) + " "
        stringy_thingy += "1\n"
        n -= 1
    return stringy_thingy

def merge_dicts(d1, d2):
    new_dict = d1.copy()
    for key in d2:
        if key in new_dict:
            new_dict[key] = d1[key] + d2 [key]
        else:
            new_dict[key] = d2[key]
    return new_dict

print(pyramid(5))