# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(f_names, l_names):
    full_names = []
    for first in f_names:
        for last in l_names:
            full_names.append(first + " " + last)
    return full_names

first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']

print(get_names(first_names, last_names))

def average_scores(scores):
    averages = []
    for student_scores in scores:
        total = 0
        count = 0
        for score, weight in student_scores:
            total += score * weight
            count += weight
        if count == 0:
            averages.append(0)
        else:
            averages.append(total / count)
    return averages

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(scores))