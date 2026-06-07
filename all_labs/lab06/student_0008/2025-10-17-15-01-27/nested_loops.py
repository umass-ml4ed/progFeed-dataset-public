# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for i in first_names:
        for j in last_names:
            full_names.append(f'{i} {j}')
    return full_names

def average_scores(lst):
    final = []
    for i in lst:
        total = 0
        for k, j in i:
            if j == 0:
                total += k
            elif j == 1:
                total += k * 0.9
            elif j == 2:
                total += k * 0.75
            elif j == 3:
                total += k * 0.5
            else:
                total = 0
        final.append(total/len(i))
    return final