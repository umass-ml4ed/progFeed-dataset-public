# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def get_names(first_names, last_names):
    """
    Returns a list of all combinations of first and last names.
    """
    full_names = []
    for first in first_names:     
        for last in last_names:        
            full_name = first + " " + last
            full_names.append(full_name)
    return full_names


def average_scores(scores):
    """
    Returns a list of average scores for each student after applying lateness penalties.
    """
    penalties = {0: 1.0, 1: 0.9, 2: 0.75, 3: 0.5}  
    averages = []

    for student in scores:  
        total = 0
        for grade, lateness in student: 
            
            if lateness in penalties:
                multiplier = penalties[lateness]
            else:
                multiplier = 0  
            total += grade * multiplier
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

