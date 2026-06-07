# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def get_names(first_names,last_names):
   full_names = []
   for first in first_names:
        for last in last_names:
            name = first + ' ' + last
            full_names.append(name)
   return full_names





def average_scores(scores): 
    averages = []
    
    for student in scores:
        total = 0
        count = 0
        
        for grade, lateness in student:
            if lateness == 0:
                penalty = 1
            elif lateness == 1:
                penalty = 0.9
            elif lateness == 2:
                penalty = 0.75
            elif lateness == 3:
                penalty = 0.5
            else:  # lateness >= 4
                penalty = 0

            total += grade * penalty
            count += 1

    
        averages.append(total / count)
    
    return averages