# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for char in first_names:
        for char2 in last_names:
            fullname = char + ' ' + char2
            full_names.append(fullname)
    return full_names
print(get_names(['Ari', 'John'], ['Blake', 'Joe']))


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



