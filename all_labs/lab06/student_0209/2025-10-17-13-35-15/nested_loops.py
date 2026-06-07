# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names:list, last_names:list):
    full_names = []
    for i in first_names:
        for u in last_names:
            full_names.append(i + " " + u)       
    return full_names


def average_scores(students):
    result = []
    
    for student in students:
        total = 0
        count = 0
        
        
        for grade, lateness in student:
            if lateness == 0:
                penalty_factor = 1.0
            elif lateness == 1:
                penalty_factor = 0.9
            elif lateness == 2:
                penalty_factor = 0.75
            elif lateness == 3:
                penalty_factor = 0.5
            else:
                penalty_factor = 0.0
            
            total += grade * penalty_factor
            count += 1
        
        if count > 0:
            average = total / count
        else:
            average = 0
        
        result.append(average)
    
    return result



            
