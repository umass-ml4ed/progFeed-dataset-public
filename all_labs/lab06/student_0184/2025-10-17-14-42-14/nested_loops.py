# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    #first_names = ['Ari', 'Taylor']
    #last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
    full_names = []

    for first in range(len(first_names)):
        for last in range(len(last_names)):
            full_names.append(f'{first} {last}')
    return full_names

def average_scores(scores):
    average_grades = []
    for assignments in scores:
        total_penalized_grade = 0
        for grade, lateness in assignments:
            if lateness == 0:
                penalty_factor = 1.0
            elif lateness == 1:
                penalty_factor = 0.9
            elif lateness == 2:
                penalty_factor = 0.75
            elif lateness == 3:
                penalty_factor = 0.5
            else:
                penalty_factor = 0
            total_penalized_grade + grade * penalty_factor
    if len(assignments) > 0:
        average_grades.append(total_penalized_grade / len(assignments))
    else:
        average_grades.append(0)
    return average_grades

