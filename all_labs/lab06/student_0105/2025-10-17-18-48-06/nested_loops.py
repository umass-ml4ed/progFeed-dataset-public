# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']


def get_names(first_names, last_names):
    full_names = []
    for i in first_names:
        for j in range(len(last_names)):
            full_name = i, last_names[j]
            full_names.append(full_name)

    return full_names

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]


def average_scores(lst):
    score_lst = []
    for i in range(len(lst)):
        sum = 0
        for j in range(len(lst[i])):
            #for k in range(len(lst[i][j])):
            if lst[i][j][1] == 0:
                score = (lst[i][j][0])
            elif lst[i][j][1] == 1:
                score = (lst[i][j][0] * .9)
            elif lst[i][j][1] == 2:
                score = (lst[i][j][0] * .75)
            elif lst[i][j][1] == 3:
                score = (lst[i][j][0] * .5)
            elif lst[i][j][1] == 4:
                score = 0
            sum += score
            final = sum / len(lst[i])
        score_lst.append(final)
            
    return score_lst
        


