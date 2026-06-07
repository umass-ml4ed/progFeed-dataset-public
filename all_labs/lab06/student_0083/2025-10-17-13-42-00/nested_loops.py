# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for first_char in first_names:
        for last_char in last_names:
            full_names.append(first_char)
            full_names.append(last_char)
    return full_names

def average_scores(scores):
    average_grade = []
    for student_scores in scores:
        total = 0
        count = 0
        for grade, late in student_scores:
            if late == 0:
                grade *= 1
            elif late == 1:
                grade *= 0.9
            elif late == 2:
                grade *= 0.75
            elif late == 3:
                grade *= 0.5
            elif late >= 4:
                grade *= 0
            total += grade
            count += 1
        average_grade.append(total / count)
    return average_grade


print(average_scores([[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]))


