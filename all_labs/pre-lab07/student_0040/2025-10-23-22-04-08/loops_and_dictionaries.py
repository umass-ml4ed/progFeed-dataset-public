# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def pyramid(n):
    lines = []
    for i in range(n, 0, -1):
        line = " ".join(str(x) for x in range(i, 0, -1))
        lines.append(line)
    return "\n".join(lines)

def merge_dicts(d1, d2):
    result = d1.copy()
    for key, value in d2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value    
    return result