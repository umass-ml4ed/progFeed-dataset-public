# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names (first_names, last_names):
    full_names=[]
    for first in first_names [0:]:
        for last in last_names [0:]:
            full_names.append (first +' '+ last)
    return full_names
#print(get_names (['Ari', 'Taylor'], ['Levine', 'Lopez', 'Khan', 'Wang']))

def average_scores(scores):
    averages = []
    for group in scores:
        total = 0
        count = 0
        for score, lateness in group:
            if lateness == 0:
                total += score
            elif lateness == 1:
                total += score - 10
            elif lateness == 2:
                total += score - 25
            elif lateness == 3:
                total += score - 50
            else:
                total += 0 
            count += 1
        average = total / count
        averages.append (average)
    return averages
scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)],[(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print (average_scores (scores))


