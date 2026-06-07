# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def get_names(first_names, last_names):
    full_names = []
    for first in first_names:
        for last in last_names:
            full_names.append (f"{first} {last}")
    return full_names        
first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']

def average_scores (scores):
    averages = []
    for student_scores in scores:
        total_score = 0
        count = 0
        for grade, lateness in student_scores:
            if lateness == 0:
                total_score += grade
            elif lateness == 1:
                total_score += grade * 0.9
            elif lateness == 2:
                total_score += grade * 0.75
            elif lateness == 3:
                total_score += grade * 0.50
            count += 1
        average = total_score / count if count > 0 else 0
        averages.append(average)
    return averages
scores = [[(90, 0), (80,1), (70,2), (60,3), (50,4)], [(100, 10), (90,0), (80,0), (90,0)], [(0,0), (20,0), (40,1), (100,0), (100,0), (100,0)]]
print(average_scores(scores))
