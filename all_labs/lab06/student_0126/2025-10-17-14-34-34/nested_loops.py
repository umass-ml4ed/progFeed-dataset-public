# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(l1, l2):
    full_names = []
    for i in l1:
        for j in l2:
            full_names.append(str(i) + ' ' + str(j))
    return full_names

def average_scores(l):
    average = []
    for i in l:
        scores = []
        for j in i:
            if j[1] == 0:
                scores.append(j[0])
            elif j[1] == 1:
                scores.append(j[0] * .9)
            elif j[1] == 2:
                scores.append(j[0] * .75)
            elif j[1] == 3:
                scores.append(j[0] * .5)
            elif j[1] >= 0:
                scores.append(0)
        av = 0
        for score in scores:
            av += score
        av = float(av) / float(len(scores))
        average.append(av)
    return average

# print(average_scores([[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]))