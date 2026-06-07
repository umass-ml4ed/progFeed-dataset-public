# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def average_scores(students):
    averages = []
    for student in students:
        total = 0
        count = 0
        for grade, lateness in student:
            if lateness == 0:
                total += grade
                count += 1
            elif lateness == 1:
                total += grade * 0.9
                count += 1
            elif lateness == 2:
                total += grade * 0.75
                count += 1
            elif lateness == 3:
                total += grade * 0.5
                count += 1
        if count == 0:
            averages.append(0)
        else:
            averages.append(total / count)
    return averages





        
                
