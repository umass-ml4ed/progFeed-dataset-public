# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

from itertools import count


def get_names(first_names, last_names):
    full_names = []
    for first in first_names:
        for last in last_names:
            full_names.append(f"{first} {last}")
    return full_names
print(get_names(("Ari", "Taylor"), ("Levine", "Lopez")))


def average_scores(all_students):
    averages = []
    for student in all_students:
        total = 0
        count = len(student)
        for grade, lateness in student:
            if lateness == 0:
                total += grade
            elif lateness == 1:
                total += grade * 0.9
            elif lateness == 2:
                total += grade * 0.75
            elif lateness == 3:
                total += grade * 0.5
            else:
                total += 0
        averages.append(total / count)
    return averages

