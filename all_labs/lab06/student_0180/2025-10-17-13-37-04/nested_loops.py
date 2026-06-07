# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for i in range(0, len(first_names)):
        for j in range(0, len(last_names)):
            fullName = first_names[i] + ' ' + last_names[j]
            full_names.append(fullName)

    return full_names

def average_scores(lst):
    scores = []
    for j in range(0, len(lst)):
        avg1 = 0.0
        for i in range(0, len(lst[j])):
            if lst[j][i][1] == 0:
                avg1 += lst[j][i][0]
            elif lst[j][i][1] == 1:
                avg1 += lst[j][i][0] * 0.9
            elif lst[j][i][1] == 2:
                avg1 += lst[j][i][0] * 0.75
            elif lst[j][i][1] == 3:
                avg1 += lst[j][i][0] * 0.5
            else:
                avg1 += lst[j][i][0] * 0
    
        avg1 /= len(lst[j])
        scores.append(avg1)

    return scores

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(scores))






        