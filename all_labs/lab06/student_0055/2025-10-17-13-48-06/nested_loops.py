# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for f_names in first_names:
        for l_names in last_names:
            fullname = f_names + " " + l_names
            full_names.append(fullname)
    return full_names

def average_scores(scores):
    ave_scores = []
    for student in scores: #[(g,l), g2, g3 ....)
        score = 0
        student_grades = []
        for grade in student: #(rawgrade,lateness)(60,3)
            if grade[1] == 0:
                new_grade = grade[0] * 1.00
            elif grade[1] == 1:
                new_grade = grade[0] * .90
            elif grade[1] == 2:
                new_grade = grade[0] * .75
            elif grade[1] == 3:
                new_grade = grade[0] * .50
            else:
                new_grade = 0
            student_grades.append(new_grade)
        print(student_grades)
        total_score = sum(student_grades)
        ave_score = total_score/len(student)
        ave_scores.append(ave_score)
    return ave_scores
