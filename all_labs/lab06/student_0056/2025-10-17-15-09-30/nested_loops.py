# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

first_names = ['Ari', 'Taylor' ]
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']

def get_names(first_names, last_names):
    full_name = []
    for first in first_names:
        for last in last_names:
            full_names= (f"{first} {last}")
            full_name.append(full_names)
    return full_name
    

print(get_names(first_names, last_names))


scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]


def average_scores(scores):
    avrgs = []
    for students in scores:
        avrg = 0
        for assignments in students:
            grades = assignments[0]
            if assignments[1] == 0:
                avrg += grades
            elif assignments[1] ==1:
                avrg += grades * .9
            elif assignments[1] == 2:
                avrg += grades * .75
            elif assignments[1] == 3:
                avrg += grades * .5
            else:
                avrg += grades * 0
        avrg = avrg / len(students)
        avrgs.append(avrg)
    return avrgs

print(average_scores(scores))    
