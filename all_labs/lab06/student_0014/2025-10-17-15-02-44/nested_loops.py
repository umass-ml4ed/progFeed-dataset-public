# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

first_names = first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
def get_names(first_names,last_names):
    full_names = []
    for i in first_names:
        for j in last_names:
                full_names.append(i + ' ' +j)
    return full_names
print(get_names())

lst = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]

def average_scores(lst, list):
    score = []
    for i in range(lst):
        average = 0
        for a in range(lst):
            average = 0
    if [i][a][1] == 0:
        average = [i][a][0] == 0
    elif [i][a][1] == 1:
        average = [i][a][0] == 0.9
    elif [i][a][1] == 2:
        average = [i][a][0] == 0.75
    elif [i][a][1] == 3:
        average = [i][a][0] == 0.5

        score.append(average/len (lst[i]))
    return score
print(average_scores(lst))
                        
