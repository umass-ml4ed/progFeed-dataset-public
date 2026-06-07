# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED


def get_names(first_names, last_names):
    full_names = []
    for first in first_names:
        for last in last_names:
           full_name = first + " " + last 
        full_names.append(full_name)
        
    return full_names

first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']


def average_scores(scores):
    penalties = {
        0: 1.0,
        1: 0.9,
        2: 0.75,
        3: 0.5
    }
    averages = []
    for student in scores:
        total = 0
        for grade, lateness in student:
            multiplier = penalties.get(lateness, 0.0)
            total += grade * multiplier

        avg = total / len(student)
        averages.append(avg)


    return averages
        


