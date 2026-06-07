# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    """
    Prints a pyramid pattern where each line starts from n, n-1, ..., down to 1.
    Example for n=4:
    4 3 2 1
    3 2 1
    2 1
    1
    """
    result = ""
    for i in range(n, 0, -1):
        line = " ".join(str(x) for x in range(i, 0, -1))
        result += line + "\n"
    return result

def merge_dicts(d1, d2):
    """
    Merges two dictionaries.
    - If a key appears in both, sum their values.
    - Otherwise, keep the existing key-value.
    """
    merged = d1.copy()
    for key, value in d2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged

if __name__ == "__main__":
    print(pyramid(4))

    print(pyramid(5))

    print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))

    print(merge_dicts({'x': 10}, {'y': 20}))

    print(merge_dicts({}, {'a': 5}))

    print(merge_dicts({'a': 1, 'b': 2, 'c': 3}, {'b': 5, 'd': 10}))
