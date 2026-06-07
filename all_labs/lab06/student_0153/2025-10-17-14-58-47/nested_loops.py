# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']

def get_names(first_names, last_names):
    full_names = []
    for first in first_names:
        for last in last_names:
            full_names.append(f"{first} {last}")
    return full_names     
print(get_names(first_names, last_names))

scores = [
    [(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)],
    [(100, 10), (90, 0), (80, 0), (90, 0)],
    [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]
]
def average_scores(scores):
    result = []
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
        average = total / len(student)
        result.append(average)
    return result