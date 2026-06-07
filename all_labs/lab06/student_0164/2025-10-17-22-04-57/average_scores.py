# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

def average_scores(students):
    scores = [
    [(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]
    ]
    averages = []
    for i in range(len(students)):
        assignments = students [i]
        total = 0
        count = len(assignments)

        for j in range(len(assignments)):
            grade, lateness = assignments[j]
            if lateness == 0:
                penalty = 1.0
            elif lateness == 1:
                penalty = 0.9
            elif lateness == 2:
                penalty = 0.75
            elif lateness == 3:
                penalty = 0.5
            elif lateness >= 4:
                penalty = 0

            total += grade * penalty 
        average = total / count if count > 0 else 0
        average.append(average)
        return average_scores
    
    print(average_scores(scores))














