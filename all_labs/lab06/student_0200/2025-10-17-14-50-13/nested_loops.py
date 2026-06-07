# Author    : REDACTED
# Email     : REDACTED
# Spire ID  : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for first in first_names:
        for last in last_names:
            full_names.append(first + " " + last)
    return full_names
print(get_names(['Ari', 'Taylor'], ['Levine', 'Lopez', 'Khan', 'Wang']))

def average_scores(scores):
    average_grades = []
    for i in scores:
        total = 0
        for grade, day_late in i:
            if day_late == 0:
                penalty = 1.0
            elif day_late == 1:
                penalty = 0.9
            elif day_late == 2:
                penalty = 0.75
            elif day_late == 3:
                penalty = 0.5
            else:
                penalty = 0.0
            total += grade * penalty 
            average = total/len(i)
            average_grades.append(average)
    return average_grades 
scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(scores))