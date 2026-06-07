# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

def average_scores(scores):
    averages = []
    for student_scores in scores:
        total = 0
        for grade, lateness in student_scores:
            if lateness == 0:
                penalty = 1.0
            elif lateness == 1:
                penalty = 0.9
            elif lateness == 2:
                penalty == 0.75
            elif lateness == 3:
                penalty == 0.5
            else:
                penalty = 0.0
        averages.append(total / len(student_scores))
    return averages 


               




                
# scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)]], 
# [(100, 10), (90, 0), (80, 0), (90,0)], 
#[(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]



    













