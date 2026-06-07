# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def get_names(first_names, last_names):
    full_names = []
    for first_name in first_names:
        for last_name in last_names:
            full_name = f"{first_name} {last_name}"
            full_names.append(full_name)
    return full_names
def average_scores(student_assignments):
    penalty_multipliers = {
        0: 1.0,    
        1: 0.9,    
        2: 0.75,  
        3: 0.5,    
    }
    
    student_averages = []
    for student in student_assignments:
        total_grade = 0
        num_assignments = len(student)
        
        for grade, lateness in student:
            if lateness >= 4:
                multiplier = 0.0  
            else:
                multiplier = penalty_multipliers[lateness]
            
            total_grade += grade * multiplier
        
        average = total_grade / num_assignments
        student_averages.append(average)
    
    return student_averages

def average_scores(student_assignments):
    student_averages = []
    
    for student in student_assignments:
        total_grade = 0
        num_assignments = len(student)
        
        for assignment in student:
            grade, lateness = assignment
            
            
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
            
            total_grade += grade * multiplier
        
        average = total_grade / num_assignments
        student_averages.append(average)
    
    return student_averages


first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
result = get_names(first_names, last_names)
print(result)
scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(scores))
