# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []

    for f in first_names:
        for l in last_names:
            full_name = str(f) + " " + str(l)
            full_names.append(full_name)
    return full_names
            
first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']

result = get_names(first_names, last_names)
print(result)

def average_scores(scores):
    averages = []
    for s in scores:
        after_lateness = 0
        count = len(s)

        for grade, lateness in s:
            if lateness == 0:
                multiplier = 1.0
            elif lateness == 1:
                multiplier = 0.9
            elif lateness == 2:
                multiplier = 0.75
            elif lateness == 3:
                multiplier = 0.5
            else:
                multiplier = 0.0

            after_lateness += grade * multiplier
    
        average = after_lateness / count
        averages.append(average)

    return averages

scores = [
    [(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)],
    [(100, 10), (90, 0), (80, 0), (90, 0)], 
    [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]
    ]

print(average_scores(scores))