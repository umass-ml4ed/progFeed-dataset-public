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
        count = 0
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
            adjusted_grade = grade * penalty
            total += adjusted_grade
            count += 1
        if count > 0:
            average = total / count
        else:
            average = 0
        averages.append(average)
    
    return averages