# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for first in first_names:
        for last in last_names:
            full_names.append(f"{first} {last}")
    return full_names

def average_scores(lst): 
    scores = []
    for stu_lst in lst: 
        sum = 0 
        count = 0 
        for grades in stu_lst:
            grade, lateness = grades
            
            if lateness == 0:
                penalty_factor = 1.0
            elif lateness == 1:
                penalty_factor = 0.9
            elif lateness == 2:
                penalty_factor = 0.75
            elif lateness == 3:
                penalty_factor = 0.5
            else:  # lateness >= 4
                penalty_factor = 0.0
            
            sum += grade * penalty_factor
            count += 1
        
        average = sum / count
        scores.append(average)
    
    return scores

