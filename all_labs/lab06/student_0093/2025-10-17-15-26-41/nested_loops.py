# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']

def get_names(first_names, last_names):
    full_names = []
    for f in first_names:
        for l in last_names:
            full_name = f + ' ' + l
            full_names.append(full_name)
    return full_names

print(get_names(first_names, last_names))

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]

def average_scores(scores):
    averages = []
    for student in scores:
        total = 0
        for grade, lateness in student:
            if lateness == 0:
                penalty = 1.0
            elif lateness == 1:
                penalty = 0.9
            elif lateness == 2:
                penalty = 0.75
            elif lateness == 3:
                penalty = 0.5
            elif lateness >= 4:
                penalty = 0
            total += grade * penalty
        average = total / len(student)
        averages.append(average)
    return averages

print(average_scores(scores))