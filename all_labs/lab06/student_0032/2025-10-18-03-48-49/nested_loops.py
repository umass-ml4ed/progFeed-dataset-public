# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def get_names(first_names: str, last_names: str):
    full_names = []
    for first in first_names: 
        for last in last_names: 
            full_names.append(first + ' ' + last)
    return full_names 

first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']

print(get_names(first_names, last_names))

#-----------------------------

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]


def average_scores(scores):
    averages = []
    for student in scores:

        average=0

        for assignment in student:
            
            score,late=assignment
            if late==0:
                percent=1
            elif late==1:
                percent=0.9
            elif late==2:
                percent= 0.75
            elif late==3:
                percent=0.5
            elif late>=4:
                percent=0
            marks=score*percent
            total+=marks

        average=total / (len(student))

        averages.append(average)
    return averages


