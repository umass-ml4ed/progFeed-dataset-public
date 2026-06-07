# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    output = ""
    for i in range(n, 0, -1):
        nums = []
        for j in range(i, 0, -1):
            nums.append(str(j))
        output += " ".join(nums) + "\n"
    return output

def merge_dicts(d1,d2):
    dih = d1.copy()
    for key, value in d2.items():
        if key not in dih:
            dih[key] = value
        elif key in dih:
            dih[key] += value
    return dih

