# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def get_names(first_names: list, last_names: list):
    
    full_names=[]
    for i in first_names:
        for j in last_names:
            name_combo = i + ' ' + j
            full_names.append(name_combo)
    return full_names


def avergage_scores(scores: list):
    result = []

    for student in scores:
        total = 0
        num_assignments = len(student)

        for grade, late in student:
            if late == 0:
                penalty = 1
            elif late == 1:
                penalty == 0.9
            elif late == 2:
                penalty = 0.75
            elif late == 3:
                penalty = 0.5
            else: 
                penalty = 0
            total += grade * penalty

        average = total / num_assignments
        result.append(average)

    return result



