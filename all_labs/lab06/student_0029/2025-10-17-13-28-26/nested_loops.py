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

def average_scores(raw_grade, lateness):
    total_score = 0
    for score, lateness in raw_grade:
        adjusted_score = score - (lateness* 10)
        if adjusted_score < 0:
            adjusted_score = 0
        total_score += adjusted_score
    average = total_score / len(raw_grade) if raw_grade else 0
    return average

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(scores[0], 0))