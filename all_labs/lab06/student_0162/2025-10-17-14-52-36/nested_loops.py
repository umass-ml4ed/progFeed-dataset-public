# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for i in first_names:
        for j in last_names:
            a = i + ' ' + j
            full_names.append(a)
    return full_names


def average_scores(scores):
    avg_scores = []
    for i in scores:
        total = 0
        for j in i:
            a = j[0]
            b = j[1]
            if b == 0:
                total += a   
            elif b== 1:
                total += a * 0.90 
            elif b == 2:
                total += a * 0.75
            elif b == 3:
                total += a * 0.50 
            else:
                total += 0 
        avg = total / 5
        avg_scores.append(avg)
    return avg_scores

