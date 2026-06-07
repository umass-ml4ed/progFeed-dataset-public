# Authors   : REDACTED
# Emails    : REDACTED
# Spire ID REDACTED

def get_names(first_names, last_names):
    full_names = []
    for first in first_names:
        for last in last_names:
            full_name = first + " " + last
            full_names.append(full_name)
    return full_names

def average_scores(scores):
    averages = []
    for student in scores:
        total = 0
        count = 0
        for grade, lateness in student:
            # Apply lateness penalty
            if lateness == 0:
                credit = 1.0
            elif lateness == 1:
                credit = 0.9
            elif lateness == 2:
                credit = 0.75
            elif lateness == 3:
                credit = 0.5
            else:
                credit = 0.0

            total += grade * credit
            count += 1

        average = total / count
        averages.append(average)
    return averages

scores = [
    [(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)],
    [(100, 10), (90, 0), (80, 0), (90, 0)],
    [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]
]

print(average_scores(scores))