# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for first in first_names:
        for last in last_names:
            full_names.append(f"{first} {last}")
    return full_names  

def average_scores(lst):
    avg_grades = []
    penalties = {
        '0': 1.0,
        '1': 0.9, 
        '2': 0.75,
        '3': 0.5,
        '4': 0.0
    }
    for student in lst:
        total = 0
        for grade, late in student:
            late = str(late)
            pen = penalties.get(late, 0.0)
            real_grade = grade * pen
            total += real_grade
        avg = total / len(student)
        avg_grades.append(avg)
    return avg_grades


print(average_scores([[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]))