# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    fullnames = []
    i=0
    x=0
    for i in range(len(first_names)):
        for x in range(len(last_names)):
            fullnames.append(first_names[i] + ' ' + last_names[x])
        
    return fullnames


first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']

full_names = get_names(first_names, last_names)
print(full_names)



def average_scores(scores):
    penalty_map = {
        0: 1.0,    
        1: 0.9,    
        2: 0.75,   
        3: 0.5,    
    }
    
    averages = []
    
    for student_assignments in scores:
        total = 0
        for grade, lateness in student_assignments:
            if lateness >= 4:
                penalized_grade = 0  
            else:
                penalty = penalty_map.get(lateness, 0)
                penalized_grade = grade * penalty
            total += penalized_grade
        avg = total / len(student_assignments)
        averages.append(avg)
    return averages

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(scores))