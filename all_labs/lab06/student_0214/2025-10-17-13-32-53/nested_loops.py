# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def get_names(first_names, last_names):
    full_names = []
    for name in first_names:
        for last_name in last_names:
            the_name = name + " " + last_name
            full_names.append(the_name)
    return full_names

def average_scores(scores):
    average = []
    for student in scores:
        sum = 0
        for grade in student:
            if grade[1] == 1:
                score = grade[0] * 0.9
            elif grade[1] == 2:
                score = grade[0] * 0.75
            elif grade[1] == 3:
                score = grade[0] * 0.5
            elif grade[1] >= 4:
                score = 0
            else:
                score = grade[0]
            sum += score
        student_average = sum / len(student)
        average.append(student_average) 
    return average
scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(scores))