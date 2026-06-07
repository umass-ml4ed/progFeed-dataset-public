# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]

def get_names(first_names, last_names):
    full_names = []
    for i in range(len(first_names)):
        for j in range(len(last_names)):
            full_name = first_names[i] + " " + last_names[j]
            full_names.append(full_name)
    return full_names


def average_scores(scores):
    averages = []
    for i in range(len(scores)):      
        total = 0
        count = len(scores[i])
        for j in range(len(scores[i])): 
            grade = scores[i][j][0]
            lateness = scores[i][j][1]

            if lateness == 0:
                new_grade = grade
            elif lateness == 1:
                new_grade = grade * 0.90
            elif lateness == 2:
                new_grade = grade * 0.75
            elif lateness == 3:
                new_grade = grade * 0.50
            elif lateness >= 4:
                new_grade = grade * 0
            total += new_grade

        averages.append(total / count)
    return averages


print(average_scores(scores))
