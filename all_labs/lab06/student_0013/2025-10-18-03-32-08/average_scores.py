# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def average_scores(scores):
    result = []

    for student in scores:
        total = 0
        for grade, late in student:
            if late == 0:
                total += grade * 1
            elif late == 1:
                total += grade * 0.9
            elif late == 2:
                total += grade * 0.75
            elif late == 3:
                total += grade * 0.5
            else:
                total += 0
        average = total / len(student)
        result.append(average)
    
    return result


scores = [
    [(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)],
    [(100, 10), (90, 0), (80, 0), (90, 0)],
    [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]
]

print(average_scores(scores))
