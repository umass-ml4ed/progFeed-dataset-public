# Author  : REDACTED
# Email : REDACTED
# Spire ID  : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for f in first_names:
        for l in last_names:
            combo = f + ' ' + l
            full_names.append(combo)
    return full_names

print(get_names(['Ari', 'Taylor'], ['Levine', 'Lopez', 'Khan', 'Wang']))


def average_scores(scores):
    averages = []
    
    for student in scores:
        total = 0
        for grade, lateness in student:
            if lateness == 0:
                adjusted = grade
            elif lateness == 1:
                adjusted = grade * 0.9
            elif lateness == 2:
                adjusted = grade * 0.75
            elif lateness == 3:
                adjusted = grade * 0.5
            else:
                adjusted = 0
            total += adjusted
        average = total / len(student)
        averages.append(average)
        
    return averages
