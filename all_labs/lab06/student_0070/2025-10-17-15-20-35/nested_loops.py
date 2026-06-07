# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for first in first_names:
        for last in last_names:
            full_names.append(first + ' ' + last)
    return full_names

def average_scores(students_assignments):
    averages = []
    for assignments in students_assignments:
        total_score = 0
        for grade, lateness in assignments:
            if lateness == 0:
                total_score += grade
            elif lateness == 1:
                total_score += grade * 0.9
            elif lateness == 2:
                total_score += grade * 0.75
            elif lateness == 3:
                total_score += grade * 0.5
            else:
                total_score += 0
        average = total_score / len(assignments) if assignments else 0
        averages.append(average)
    return averages