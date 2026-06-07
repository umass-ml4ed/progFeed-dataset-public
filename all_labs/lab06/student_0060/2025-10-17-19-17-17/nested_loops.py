# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def get_names(first_names ,last_names):
   full_names = []
   for first in first_names:
        for last in last_names:
            name = first + ' ' + last
            full_names.append(name)
   return full_names




scores = [
    [(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
    [(100, 10), (90, 0), (80, 0), (90, 0)], 
    [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]
]

def average_scores(scores): 
    average = []
    for students in scores:
        total = 0 
        assignment = 0
        for (grade, lateness) in students:
            if lateness == 0:
                penalty = 1
            elif lateness == 1: 
                penalty = .9
            elif lateness == 2:
                penalty = .75
            elif lateness == 3:
                penalty = .5
            else:
                penalty = 0
            total += grade * penalty
            assignment += 1 
    average.append(total/ assignment)
    
    return average

print(average_scores(scores))