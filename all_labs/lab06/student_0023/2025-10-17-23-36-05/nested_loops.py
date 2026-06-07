# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for first in first_names:
        for last in last_names:
            full_names.append(f"{first} {last}")
    return full_names

def average_scores(students_scores):
    result = []
    for student in students_scores:
        total = 0
        n = len(student)
        for grade, lateness in student:
            if lateness == 0:
                penalty = 1.0
            elif lateness == 1:
                penalty = 0.9
            elif lateness == 2:
                penalty = 0.75
            elif lateness == 3:
                penalty = 0.5
            else:
                penalty = 0.0
            total += grade * penalty
        average = total / n
        result.append(average)
    return result
