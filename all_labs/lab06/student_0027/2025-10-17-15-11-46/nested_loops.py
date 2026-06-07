# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for first in first_names:
        for last in last_names:
            full_names.append(f"{first} {last}")
    return full_names


def average_scores(students):
    averages = []
    for student in students:
        total = 0
        count = 0
        for grade, late in student:
            if late == 0:
                penalty = 1.0
            elif late == 1:
                penalty = 0.9
            elif late == 2:
                penalty = 0.75
            elif late == 3:
                penalty = 0.5
            else:
                penalty = 0.0
            total += grade * penalty
            count += 1
        avg = total / count if count > 0 else 0
        averages.append(avg)
    return averages
