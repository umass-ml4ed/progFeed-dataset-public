# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def get_names(first_names, last_names):
    full_names = []
    for i in first_names:
        for a in last_names:
            full_names.append(i + " " + a)
    return full_names

#first_names = ['Ari', 'Taylor']
#last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
#print(get_names(first_names, last_names))


def average_scores(lst_of_lsts):
    scores = []
    average = 0
    for i in range(len(lst_of_lsts)):
        average = 0
        for a in range(len(lst_of_lsts[i])):
            if lst_of_lsts[i][a][1] == 0:
                average += lst_of_lsts[i][a][0]
            elif lst_of_lsts [i][a][1] == 1:
                average += lst_of_lsts[i][a][0] * 0.90
            elif lst_of_lsts[i][a][1] == 2:
                average += lst_of_lsts[i][a][0] * 0.75
            elif lst_of_lsts[i][a][1] == 3:
                average += lst_of_lsts[i][a][0] * 0.50
            else:
                average += lst_of_lsts[i][a][1] * 0
        scores.append(average/len(lst_of_lsts[i]))
    return scores

#scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          #[(100, 10), (90, 0), (80, 0), (90, 0)], 
          #[(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
#print(average_scores(scores))