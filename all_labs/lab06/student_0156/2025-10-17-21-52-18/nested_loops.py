# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

first_names = ['Susie','Enzo']
last_names = ['Nguyen','Ho','Do']

def get_names(first_names,last_names):
    full_names = []
    for first in first_names:
        for last in last_names:
            full_name = first + " " + last
            full_names.append(full_name)
    return full_names

print(get_names(first_names, last_names))

def average_scores(students):
    averages = []
    
    for assignments in students:
        total = 0
        count = 0
        
        for grade, lateness in assignments:
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
            
            adjusted_grade = grade * penalty
            total += adjusted_grade
            count += 1
        
        if count > 0:
            avg = total / count
        else:
            avg = 0

        averages.append(avg)

    return(averages)
        
scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]


print(average_scores(scores))
