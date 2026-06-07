# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang'] 
def get_names(first_names, last_names):
    full_names = []

    for first in first_names:
        for last in last_names:
            full_names.append(first + " " + last)
    return full_names

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]

print(get_names(first_names, last_names))

def average_scores(scores):
    result = []
    for student in scores:
        total = 0
        for grade, lateness in student:
            if lateness == 0: 
                total += grade * 1.0
            elif lateness == 1:
                total += grade * 0.9
            elif lateness == 2:
                total += grade * 0.75
            elif lateness == 3:
                total += grade * 0.5
            else:
                total += grade * 0
        avg = total / len(student)
        result.append(avg)
    return result

print(average_scores(scores))

