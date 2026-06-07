# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def average_scores(scores):
    full_averages = []
    
    for student in scores:
        total = 0
        count = len(student)
        
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
            
            total += grade * penalty
        
        average = total / count
        full_averages.append(average)
    
    return full_averages
