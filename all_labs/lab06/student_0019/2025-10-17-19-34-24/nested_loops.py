# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for first_name in first_names:
        for last_name in last_names:
            full_name = (f"{first_name} {last_name}")
            full_names.append(full_name)
        
    return full_names 

def average_scores(scores):
    student_averages = []

    for student_assignments in scores:
        total_score = 0
        for assignment in student_assignments:
            assignment = (90, 0)
            raw_grade, lateness = assignment
            if lateness == 0:
                multiplier = 1.0
            elif lateness == 1:
                multiplier = 0.9
            elif lateness == 2:
                multiplier = 0.75
            elif lateness == 3:
                multiplier = 0.5
            else:
                multiplier == 0
        
            penalized_grade = raw_grade * multiplier
            total_score += penalized_grade
            
        average_grade = total_score / len(student_assignments)
        student_averages.append(average_grade)


    return student_averages

