# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names (first_names, last_names):
    first_names = ['Ari', 'Taylor']
    last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
    full_names=[]
    for first in first_names [0:]:
        for last in last_names [0:]:
            full_names.append (first +' '+ last)
    return full_names
print (get_names (['Ari', 'Taylor'], ['Levine', 'Lopez', 'Khan', 'Wang']))

def average_scores (scores):
    grade = 0
    for score in scores:
        if scores[0][1] == 0:
             grade = grade + score
scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
#print (average_scores (scores))