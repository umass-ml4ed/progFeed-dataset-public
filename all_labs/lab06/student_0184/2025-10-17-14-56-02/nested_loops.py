# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for first in first_names:
        for last in last_names:
            full_name = first + ' ' + last
            full_names.append(full_name)
    return full_names

def average_scores(scores):
    penalties = {
        0: 1.0,
        1: 0.9,
        2: 0.75,
        3: 0.5
    }

    result = []

    for student in scores:
        total = 0
        for grade, lateness in student:
            multiplier = penalties.get(lateness, 0)  # Default to 0 for lateness >= 4
            total += grade * multiplier
        average = total / len(student)
        result.append(average)

    return result