# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def pyramid(n):
    a_list = [a for a in range(1, n + 1)]
    a_list.reverse()
    to_print_string = ''
    while True:
        helpful_list = [str(num) for num in a_list]
        to_print_string = to_print_string + ' '.join(helpful_list)
        a_list.pop(0)
        to_print_string = to_print_string + '\n'
        if len(a_list) == 0:
            break
        #to_print_string = to_print_string + '\n'
    return to_print_string

print(pyramid(4))

def merge_dicts(dict1, dict2):
    new_dict = {}
    all_the_keys = set([key for key in dict1] + [key for key in dict2])
    for key in all_the_keys:
        if key in dict1 and key in dict2:
            new_dict[key] = dict1[key] + dict2[key]
        elif key in dict1:
            new_dict[key] = dict1[key]
        else:
            new_dict[key] = dict2[key]
    return new_dict