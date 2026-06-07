# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def get_names(lst1, lst2):
    full_names = []
    for i in lst1:
        for j in lst2:
            full_names.append(f'{i} + {j}')
    return full_names

def average_scores(list):
    avg = []
    for i in list:
        score = []
        for j in i:
            if j[1] == 0:
                score.append(j[0])
            elif j[1] == 1:
                score.append(j[0]*0.9)
            elif j[1] == 2:
                score.append(j[0]*0.75)
            elif j[1] == 3:
                score.append(j[0]*0.5)
            else:
                score.append(0)
            
        avg.append(sum(score)/len(score))
    return avg

