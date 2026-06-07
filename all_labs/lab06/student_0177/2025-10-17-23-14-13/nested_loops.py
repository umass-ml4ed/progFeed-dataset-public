# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
def get_names(first_names, last_names):
    full_names = []
    for first in first_names:          
        for last in last_names:        
            full_names.append(first + " " + last)
    return full_names

def average_scores(scores):
    result = []
    for student in scores:                  
        total = 0
        for grade, late in student:         
            if late == 0:
                credit = 1.0
            elif late == 1:
                credit = 0.9
            elif late == 2:
                credit = 0.75
            elif late == 3:
                credit = 0.5
            else:
                credit = 0.0
            total += grade * credit
        avg = total / len(student)
        result.append(avg)
    return result
