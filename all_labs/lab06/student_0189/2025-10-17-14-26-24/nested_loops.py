# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED



def get_names(first_names, last_names):
    full_names = []  
    for first in first_names:
        for last in last_names:
            full_names.append(first + " " + last)
    return full_names

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
        for grade, late in student:
            if late in penalties:
                factor = penalties[late]
            else:
                factor = 0.0
            total += grade * factor
        avg = total / len(student)
        averages.append(avg)
    return averages


first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
print(get_names(first_names, last_names))

scores = [
    [(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)],
    [(100, 10), (90, 0), (80, 0), (90, 0)],
    [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]
]
print(average_scores(scores))
