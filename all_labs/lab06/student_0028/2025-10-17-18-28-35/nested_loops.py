# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for first in first_names:               
        for last in last_names:             
            full_name = first + " " + last  
            full_names.append(full_name)    
    return full_names


def average_scores(all_students):
    averages = []
    for student in all_students:
        total = 0
        for grade, lateness in student:
            if lateness == 0:
                multiplier = 1.0
            elif lateness == 1:
                multiplier = 0.9
            elif lateness == 2:
                multiplier = 0.75
            elif lateness == 3:
                multiplier = 0.5
            else:  
                multiplier = 0.0
            total = total + (grade * multiplier)
        averages.append(total / len(student))
    return averages
