# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for a in first_names:
        for b in last_names:
            full_names.append(a + " " + b)
    return full_names

first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
print(get_names(first_names, last_names))

def average_scores(given):
    penalty = 0
    list = []
    for student in given:
        count = 0
        score = []
        for grade in student:
            if grade[1] == 0:
                penalty = 1
            elif grade[1] == 1:
                penalty = 0.9
            elif grade[1] == 2:
                penalty = 0.75
            elif grade[1] == 3:
                penalty = 0.5
            else:
                penalty = 0
            score.append(grade[0] * penalty)
        count += 1
        if student[count]:
            grade = 0
            for point in score:
                grade += point
            grade = grade / len(score)
        list.append(grade)
    return list

print(average_scores([[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]))