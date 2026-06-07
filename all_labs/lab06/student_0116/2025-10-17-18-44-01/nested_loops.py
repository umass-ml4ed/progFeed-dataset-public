# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for first in first_names:
        for last in last_names:
            full_names.append(first + " " + last)
    return full_names

def average_scores(scores):
    averages = []
    for student in scores:
        total = 0
        for grade, late in student:
            if late == 0:
                penalty = 1
            elif late == 1:
                penalty = 0.9
            elif late == 2:
                penalty = 0.75
            elif late == 3:
                penalty = 0.5
            else:
                penalty = 0
            total += grade * penalty
        averages.append(total / len(student))
    return averages


