# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def get_names(first_names,last_names):
    full_names = []
    for first in first_names:
        for last in last_names:
            full_names.append(f'{first} {last}')
    return full_names

    
def average_scores(scores):
    averages = []
    for student in scores:
        result = 0
    for grade, lateness in student:
        if lateness == 0:
            result += grade
        elif lateness == 1:
            result += grade*0.9
        elif lateness == 2:
            result += grade*0.75
        elif lateness == 3:
            result += grade*0.5
        else:
            result += 0
    averages.append(result/len(student))
    return averages