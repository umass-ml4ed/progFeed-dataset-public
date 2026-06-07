# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']

def get_names(first_names, last_names):
    full_names= []
    for f in first_names:
        for l in last_names:
            full_names.append((f + " "+ l))
    return full_names


scores=[[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]

def average_scores(scores):
    final= []
    for s in scores:
        grades= []
        for g, l in s:
                if (l == 0):
                    f= g
                elif(l == 1):
                    f = g * 0.9
                elif (l == 2):
                    f = g * 0.75
                elif (l == 3):
                    f = g * 0.5
                elif (l == 4):
                    f = 0
                grades.append(f)
        avg= sum(grades) / len(grades)
        final.append(avg)
    return final

print(average_scores(scores))
