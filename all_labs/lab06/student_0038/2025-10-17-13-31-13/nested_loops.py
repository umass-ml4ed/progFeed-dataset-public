#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']

def get_names(first_names, last_names):
    full_names = []
    for i in range(len(first_names)):
        for last in last_names:
            full_names.append(first_names[i] + " " + last)
    return full_names
print(get_names(first_names, last_names))

grade_lateness = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
def average_scores(student_assignments):
    student_averages = []
    for assignment in student_assignments:
        for i in range(len(assignment)):
            score = assignment[i][0]
            lateness = assignment[i][1]
            adjusted_scores = []
            if lateness == 0:
                score = score
                adjusted_scores.append(score)
            elif lateness == 1:
                score = (score * 0.9)
                adjusted_scores.append(score)
            elif lateness == 2:
                score = (score * 0.75)
                adjusted_scores.append(score)
            elif lateness == 3:
                score = (score * 0.5)
                adjusted_scores.append(score)
            elif lateness >= 4:
                score = 0
                adjusted_scores.append(score)
        average_score = sum(adjusted_scores) / len(adjusted_scores)
        student_averages.append(average_score)
    return student_averages

print(average_scores(grade_lateness))