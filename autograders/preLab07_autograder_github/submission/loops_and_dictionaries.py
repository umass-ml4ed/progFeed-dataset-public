#returns the pyramid pattern as a string
def pyramid(n):
    ret = ""
    for start in range(n, 0, -1):
        line = [str(i) for i in range(start, 0, -1)]
        ret += " ".join(line) + "\n"
    return ret

def merge_dicts(d1, d2):
    result = d1.copy()
    for key, value in d2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result


if __name__ == "__main__":
    print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
    print(merge_dicts({'x': 10}, {'y': 20}))
    print(merge_dicts({}, {'a': 5}))
    print(merge_dicts({'a': 1, 'b': 2, 'c': 3}, {'b': 5, 'd': 10}))
    print("Example 1:")
    print(pyramid(4))
    print("\nExample 2:")
    print(pyramid(5))
