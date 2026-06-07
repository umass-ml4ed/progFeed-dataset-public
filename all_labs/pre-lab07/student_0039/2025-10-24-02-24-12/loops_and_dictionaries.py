#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def pyramid(n) -> str: 
    pyramid_to_return = ''
    for number in range(n, 0, -1):
        for numb in range(number, 0, -1):
            pyramid_to_return += str(numb)
            if numb != 1:
              pyramid_to_return += ' '
        pyramid_to_return += '\n'
    return pyramid_to_return

def merge_dicts(d1: dict, d2: dict) -> dict:
    dict_to_return = d1.copy()
    for key in d2:
        if key in dict_to_return:
            dict_to_return[key] += d2[key]
            continue
        update =[(key, d2[key])]
        dict_to_return.update(update)
    return dict_to_return

print(pyramid(10))