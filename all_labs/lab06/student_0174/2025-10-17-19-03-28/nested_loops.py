
# Author : REDACTED
# Email : REDACTED
# SPIRE ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for first_name in first_names:
        for last_name in last_names:
            full_names.append(first_name + " " + last_name)
        return full_names
    
def average_scores(scores):
    averages = []
    for student in scores:
        total = 0
        for grade, lateness in student:
            if lateness == 0:
                penalty = 1.0
            elif lateness == 1:
                penalty = 0.9
            elif lateness == 2:
                penalty = 0.75
            elif lateness == 3:
                penalty = 0.5
            else:
                penalty = 0.0
            total = grade * penalty
            averages.append(total)
    return averages
        
    