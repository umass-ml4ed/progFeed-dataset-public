# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
scores=[[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
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






        
                
