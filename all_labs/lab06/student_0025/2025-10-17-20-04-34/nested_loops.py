# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names=[]

    for fn in first_names:
        for ln in last_names:
            full_names.append(fn + ' ' + ln)
    return full_names


def average_scores(scores):
    averages = []
    for student in scores:
        total = 0
        for grade, lateness in student:
            if lateness == 0:
                total += grade
            elif lateness == 1:
                total += grade * 0.9
            elif lateness == 2:
                total += grade * 0.75
            elif lateness == 3:
                total += grade * 0.5
            elif lateness >= 4:
                total += 0
        averages.append(total/ len(student))
    return averages

scores = [
    [(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)],
    [(100, 10), (90, 0), (80, 0), (90, 0)],
    [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]
]

print(average_scores(scores))