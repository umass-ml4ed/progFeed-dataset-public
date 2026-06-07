# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for first_name in first_names:
        for last_name in last_names:
            full_names.append(f"{first_name} {last_name}")
    return full_names

def average_scores(l):
    l_grades = []
    for student_grades in l:
        total_grade = 0
        for grade in student_grades:
            main_grade = 0
            if grade[1] >= 4:
                main_grade = grade[0] * 0
            elif grade[1] == 3:
                main_grade = grade[0] * 0.5
            elif grade[1] == 2:
                main_grade = grade[0] * 0.75
            elif grade[1] == 1:
                main_grade = grade[0] * 0.9
            elif grade[1] == 0:
                main_grade = grade[0]
            total_grade += main_grade
        avg_grade = total_grade/len(student_grades)
        l_grades.append(avg_grade)
    return l_grades