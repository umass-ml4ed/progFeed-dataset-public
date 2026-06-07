# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
def get_names(first_names: list, last_names: list):
    full_names = []
    for fname in first_names:
        for lname in last_names:
            full_names.append(f"{fname} {lname}")
    return full_names

#first_names = ['Ari', 'Taylor']
#last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
#print(get_names(first_names, last_names))

def average_scores(scores: list):
    penalties = {
        0: 1.0,
        1: 0.9,
        2: 0.75,
        3: 0.5,
    }
    student_averages = []
    for student_score in scores:
        total = 0
        for raw_grade, lateness in scores:
            deduction = penalties.get(lateness, 0.0)
            total+= raw_grade*deduction
        if student_score:
            average = total/len(student_score)
            student_averages.append(average)
        else:
            student_averages.append(0)
    return student_averages



listofscores: [[(90,0), (80,1), (70,2), (60, 3), (50,4)],
               [(100,10), (90, 0), (80, 0), (90, 0)]]

print(average_scores(listofscores))