# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names,last_names):
    full_names=[]
    for first in first_names:
        for last in (last_names):
            full_names.append( first+" " + last)
    return full_names

def average_scores(student_scores):
    averages = []
    
    for student in student_scores:
        total = 0
        for assignment in student:
            grade = assignment[0]    # first element of the tuple
            lateness = assignment[1] # second element of the tuple
            
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