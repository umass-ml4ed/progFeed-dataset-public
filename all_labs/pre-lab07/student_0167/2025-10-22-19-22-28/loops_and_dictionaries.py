# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):

    if n <= 0:
        return ""
    lines = []
    for start in range(n, 0, -1):
        lines.append(" ".join(str(i) for i in range(start, 0, -1)))
    return "\n".join(lines) + "\n"


def merge_dicts(d1,d2):
    result = d1.copy()
    for k, v in d2.items():
        result[k] = result.get(k, 0) + v
    return result

pyramid(5)