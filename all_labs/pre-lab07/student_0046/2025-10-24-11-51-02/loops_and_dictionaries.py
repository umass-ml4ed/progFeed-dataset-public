# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    """Return a string pyramid per spec and end with a newline."""
    if n <= 0:
        return ""
    lines = []
    for start in range(n, 0, -1):
        lines.append(' '.join(str(k) for k in range(start, 0, -1)))
    return '\n'.join(lines) + '\n'


def merge_dicts(d1, d2):
    """Merge two dicts, summing values on overlapping keys."""
    out = d1.copy()
    for k, v in d2.items():
        out[k] = out.get(k, 0) + v
    return out


if __name__ == "__main__":
    print(pyramid(4))
    print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))  # {'a': 1, 'b': 5, 'c': 4}
    print(merge_dicts({'x': 10}, {'y': 20}))                # {'x': 10, 'y': 20}
    print(merge_dicts({}, {'a': 5}))                        # {'a': 5}
    print(merge_dicts({'a': 1, 'b': 2, 'c': 3}, {'b': 5, 'd': 10}))  # {'a': 1, 'b': 7, 'c': 3, 'd': 10}
