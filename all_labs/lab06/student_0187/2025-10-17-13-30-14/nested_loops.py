# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names,last_names):
    full_names = []
    for i in first_names:
        for j in last_names:
            full_names.append(i+" "+j)
    return full_names

def average_scores(grade):
    result = []
    for student in grade:                     
        sum = 0
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
                penalty = 0
            sum  += grade * penalty
        average = sum / len(student)
        result.append(average)
    return result

#first_names = ['Ari', 'Taylor']
#last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
#print(get_names(first_names, last_names))
    
#scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)],[(100, 10), (90, 0), (80, 0), (90, 0)],
#        [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
#print(average_scores(scores))
    

