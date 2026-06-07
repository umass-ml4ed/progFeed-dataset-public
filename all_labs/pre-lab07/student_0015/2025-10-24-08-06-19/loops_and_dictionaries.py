# Author: REDACTED
# Email: REDACTED
# SPIRE ID: REDACTED


# 1. pyramid(n)
def pyramid(n):
    """Prints a number pyramid decreasing each line."""
    result = ""
    for i in range(n, 0, -1):  # start from n down to 1
        line = " ".join(str(x) for x in range(i, 0, -1))
        result += line + "\n"
    return result.strip()  # remove extra newline at the end


# 2. merge_dicts(d1, d2)
def merge_dicts(d1, d2):
    """Merges two dictionaries, summing values of overlapping keys."""
    merged = d1.copy()  # make a copy so we don’t change d1
    for key, value in d2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged


# Example test runs (you can comment these out before submitting)
if __name__ == "__main__":
    print(pyramid(4))
    print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
