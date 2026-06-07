# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first, last):
    full_names = []
    for i in first:
        for l in last:
            full_names.append(f"{i} {l}")
    return full_names

def average_scores(lst):
    lateness = {0:1, 1:.9, 2:.75, 3:.5, 4:0}
    scores = []
    score=0
    n=0
    for i in lst:
        for l in range(len(i)):
            n+=1
            try:
                score+=(i[l][0]*lateness[i[l][1]])
                
            except:
                continue

        scores.append(score/n)
        n=0
        score=0
    return scores