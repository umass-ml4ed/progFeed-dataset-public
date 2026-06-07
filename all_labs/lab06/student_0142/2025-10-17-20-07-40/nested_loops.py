# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for first in first_names:
        for last in last_names:
            full_names.append(f"{first} {last}")
    return full_names

def average_scores(scores_list):
    averages = []
    for student in scores_list:
        total = 0
        count = len(student)
        for grade, lateness in student:
            if lateness == 0:
                credit = 1.0
            elif lateness == 1:
                credit = 0.9
            elif lateness == 2:
                credit = 0.75
            elif lateness == 3:
                credit = 0.5
            else:  # lateness >= 4
                credit = 0.0
            total += grade * credit
        averages.append(total / count if count > 0 else 0)
    return averages



