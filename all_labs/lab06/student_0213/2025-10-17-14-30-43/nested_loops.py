# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(given_names, surnames):
    full_names = []
    for name in given_names:
        for namey in surnames:
            full_names.append(f'{name} {namey}', end=' ')
    return full_names

def average_scores(in_lst):
    average_scores = []
    average = 0
    for student in in_lst:
        for grade in student:
            if grade[1] == 0:
                final_grade = grade[0]
            if grade[1] == 1:
                final_grade = grade[0] * 0.9
            if grade[1] == 2:
                final_grade = grade[0] * 0.75
            if grade[1] == 3:
                final_grade = grade[0] * 0.5
            if grade[1] >= 4:
                final_grade = 0
            average += final_grade
        average2 = average / len(student)
        average_scores.append(average2)
    return average_scores