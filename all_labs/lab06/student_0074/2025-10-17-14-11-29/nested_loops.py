# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def get_names(first_names,last_names):
    full_names = []

    for i in first_names:
        for j in last_names:
            full_names.append(i + ' ' + j)
    return full_names

first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
print(get_names(first_names,last_names))


def average_scores(scores):
    res = []

    for i in scores: 
        tot = 0

        for grade, late in i: 
            if late == 0:
                tot += grade * 1
            elif late == 1:
                tot += grade * 0.9
            elif late == 2:
                tot += grade * 0.75
            elif late == 3:
                tot += grade * 0.5
            else:
                tot += grade * 0

        average_score = tot / len(i)
        res.append(average_score)

    return res

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)],
          [(100, 10), (90, 0), (80, 0), (90, 0)],
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]
         ]
print(average_scores(scores))
