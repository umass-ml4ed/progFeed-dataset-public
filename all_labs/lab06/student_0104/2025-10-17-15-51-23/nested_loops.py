# Author    : REDACTED
# Email     : REDACTED
# Spire ID  : REDACTED


def get_names(first_names, last_names):
    full_names = []
    
    for first in first_names:
        for last in last_names:
            full_name = first + ' ' + last 
            full_names.append(full_name)
            
    return full_names

first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
        
print(get_names(first_names, last_names))


def average_scores(students):
    averages = []
    
    for student in students:
        total = 0
        count = 0
        
        for (grade, late) in student:
            if late == 0:
                penalty = 1.0
            elif late == 1:
                penalty = 0.9
            elif late == 2:
                penalty = 0.75
            elif late == 3:
                penalty = 0.5 
            else:
                penalty = 0.0
                
            total += grade * penalty
            count += 1
        
        avgperstudent = total / count
        averages.append(avgperstudent)
        
    return averages
    

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(scores))