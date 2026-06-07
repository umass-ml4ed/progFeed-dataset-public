# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def get_names(first_names, last_names):
    full_names = [] 

    for first in first_names:          
        for last in last_names:        
            full_name = first + " " + last
            full_names.append(full_name)

    return full_names


def average_scores(students):
    averages = []  
    
    for student in students:
        total = 0
        for grade, lateness in student:
            if lateness == 0:
                total += grade
            elif lateness == 1:
                total += grade * 0.9
            elif lateness == 2:
                total += grade * 0.75
            elif lateness == 3:
                total += grade * 0.5
            else:  
                total += 0
        averages.append(total / len(student))
    
    return averages

