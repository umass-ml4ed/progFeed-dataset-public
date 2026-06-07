# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for name in first_names:
        for names in last_names:
            full_names.append(f"{name} {names}")
    return full_names

def average_scores(lst):
    scores = []
    for list in lst:
        total = 0
        for i in list:
            if i[1] == 0:
                total += (i[0])
            if i[1] == 1:
                total += (i[0] *.9)
            if i[1] == 2:
                total += (i[0] *.75)
            if i[1] == 3:
                total += (i[0] *.5)
            if i[1] == 4:
                total += (i[0] * 0)
        scores.append(total/len(list))  
    return scores
 