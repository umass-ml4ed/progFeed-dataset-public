# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names (first_names, last_names):
    full_names = []
    for first_name in first_names:
        for last_name in last_names:
            new_name = first_name +' '+ last_name
            full_names.append(new_name)
    return full_names


def average_scores(student_scores):
    average_grades = []
    for student in student_scores:
        credit = 0 
        for assignment in student:
            if assignment [1] == 0:
                credit += assignment [0]
            elif assignment [1] == 1:
                credit += assignment[0] * 0.90
            elif assignment [1] == 2:
                credit += assignment [0] * 0.75
            elif assignment [1] == 3: 
                credit += assignment [0] * 0.50
            elif assignment [1] >= 4:
                credit += 0 
        average_grades.append(credit/len(student))
    return average_grades








