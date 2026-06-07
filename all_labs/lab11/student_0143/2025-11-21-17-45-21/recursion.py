# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(list, local_max=0, index=0):
    if len(list) == (index):
        return local_max
    elif index == 0:
        local_max = list[index]
        local_max = max_recursive(list, local_max, index + 1)
        return local_max
    elif list[index] > local_max:
        local_max = list[index]
        return max_recursive(list, local_max, index + 1)
    else:
        return max_recursive(list, local_max, index + 1)

def funky(n):
    if n == 0 or n == 1:
        return 1
    elif n % 2 ==0:
        return 2 * funky(n // 2)
    else:
        return 1 + 2 * funky(n + 1)

def permutations(list):
    if len(list) <= 1:
        return list
    else:
        output = []
        for front in list:
            temp_list = list[:]
            temp_list.remove(front)
            output += [front + perm for perm in permutations(temp_list)]
        return output
