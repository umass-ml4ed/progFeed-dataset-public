# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def average_scores(s):
    penalties = {0: 1.0, 1: 0.9, 2: 0.75, 3: 0.5}

    avg = []
    for student in s:
        total = 0
        for grade, late in student:
            factor = penalties.get(late, 0)  # lateness >= 4 → 0 credit
            total += grade * factor
        avg.append(total / len(student))
    return avg

print(average_scores([[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]))