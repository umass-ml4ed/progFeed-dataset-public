# AUTHOR   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


# Below, please implement the combine_lists() function as specified in the pre-lab instructions.
# ----- YOUR CODE STARTS HERE -----

def combine_lists(a: list, b: list) -> list:
    a.insert(0, b[0])
    a.append(b[-1])
    # if you want to insert it after the last element you have to use append
    # insert always insert before the element at index x

    a.pop(len(a) // 2)
    return a

# print(combine_lists([1, 2, 3, 4, 5],[4, 5, 6, 7]))



def classify_by_length(a: list) -> str:
    if len(a) == 0:
        return "empty"
    elif len(a) % 2 == 0:
        return "even_length"
    elif len(a) % 2 != 0:
        return "odd_length"
    
# print(classify_by_length([1, 2, 3]))
# print(classify_by_length([1, 2, 2, 3]))
# print(classify_by_length([]))



