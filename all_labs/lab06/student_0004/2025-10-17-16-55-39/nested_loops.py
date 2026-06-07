# Author : REDACTED
# Email  : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for first in first_names:
        for last in last_names:
            full_names.append(first + " " + last)
    return full_names


def average_scores(students):
    def weight(lateness):
        if lateness == 0:
            return 1.0
        elif lateness == 1:
            return 0.9
        elif lateness == 2:
            return 0.75
        elif lateness == 3:
            return 0.5
        else:
            return 0.0

    avgs = []
    for assignments in students:
        if not assignments:
            avgs.append(0.0)
            continue
        total = 0
        for grade, late in assignments:
            total += grade * weight(late)
        avgs.append(total / len(assignments))
    return avgs