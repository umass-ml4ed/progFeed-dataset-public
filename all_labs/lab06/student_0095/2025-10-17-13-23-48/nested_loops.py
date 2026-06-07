# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def get_names(first_names, last_names):
    full_names = []
    for first in first_names:
        for last in last_names:
            full_name = first + " " + last
            full_names.append(full_name)
    return full_names

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]


def average_scores(scores):
    result = []

    for student in scores:
        total = 0

        for grade, lateness in student:
            if lateness == 0:
                final = grade
            elif lateness == 1:
                final = grade * 0.9
            elif lateness == 2:
                final = grade * 0.75
            elif lateness == 3:
                final = grade * 0.5
            else:
                final = 0

            total += final

        average = total / len(student)
        result.append(average)

    return result

print(average_scores(scores))