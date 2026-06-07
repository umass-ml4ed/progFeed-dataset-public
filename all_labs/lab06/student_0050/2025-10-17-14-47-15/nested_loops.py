# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]

def get_names(first_names, last_names):
    full_names=[]
    for i in range(len(first_names)):
        for j in range(len(last_names)):
            full_names.append(first_names[i]+" "+last_names[j])
    return full_names

def average_scores(scores):
    ans = []
    for i in range(len(scores)):
        score = scores[i][0]
        penalty = scores[i][1]

        if penalty == 1:
            new_grade = score * 0.90
        elif penalty == 2:
            new_grade = score * 0.75
        elif penalty == 3:
            new_grade = score * 0.50
        elif penalty >= 4:
            new_grade = score * 0
        else:
            new_grade = score

        ans.append(new_grade)
    return ans


print(average_scores(scores))
