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
    as_grade = 0
    avg_grade = 0
    l_grades = []
    for student_grades in l:
        for grade in student_grades:
            credit = 0
            as_grade = 0
            if grade[1] >= 4:
                credit = 0
            elif grade[1] == 3:
                credit = 0.5
            elif grade[1] == 2:
                credit = 0.75
            elif grade[1] == 1:
                credit = 0.9
            elif grade[1] == 0:
                credit = 1
            as_grade += grade[0] * credit
        avg_grade = as_grade/len(student_grades)
        l_grades.append(avg_grade)
    return l_grades