# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n: int) -> str:
    lines = []
    for i in range(n, 0, -1):
        line = " ".join(str(x) for x in range(i, 0, -1))
        lines.append(line)
    return "\n".join(lines)


def merge_dicts(d1: dict, d2: dict) -> dict:
    merged = d1.copy()
    for key, value in d2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged



if __name__ == "__main__":
    print(pyramid(4))
    print()
    print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))