# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for i in first_names:
        for j in last_names:
            full_name = i + ' ' + j
            full_names.append(full_name)
    return full_names

def average_scores(scores):
    average_grade = []
    for student in scores:
        adjusted_grade = []
        for i in range(len(student)):
            if student[i][1] == 0:
                adjusted_grade.append(student[i][0] * 1.0)
            elif student[i][1] == 1:
               adjusted_grade.append(student[i][0] * 0.9)
            elif student[i][1] == 2:
                adjusted_grade.append(student[i][0] * 0.75)
            elif student[i][1] == 3:
                adjusted_grade.append(student[i][0] * 0.5)
            else:
                adjusted_grade.append(student[i][0] * 0.0)
        avg_value = (sum(adjusted_grade) / len(adjusted_grade))
        average_grade.append(avg_value)
    return average_grade