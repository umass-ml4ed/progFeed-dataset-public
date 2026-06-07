# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for first in first_names:
        for last in last_names:
            full_names.append(first + " " + last)
    return full_names

def average_scores(scores)
    full_averages = []
    for student in scores:
        total = 0
        for grade, late in students:
            if late == 0:
                total += grade
            elif late == 1:
                total += grade * 0.9
            elif late == 2:
                total += grade * 0.75
            elif late == 3:
                total += grade * 0.5
            else:
                total += 0
        avg = total / len(student)
        full_averages.append(avg)
    return full_averages
