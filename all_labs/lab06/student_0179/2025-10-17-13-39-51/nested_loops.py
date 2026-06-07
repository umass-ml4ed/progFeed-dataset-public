# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for first_name in first_names:
        for last_name in last_names:
            full_names.append(first_name + " " + last_name)
    return full_names

def average_scores(scores):
    output = []
    for score in scores:
        total = 0
        for student_score in score:
            if student_score[1] == 0:
                total += int(student_score[0])
            elif student_score[1] == 1:
                total += int(student_score[0]) * 0.9
            elif student_score[1] == 2:
                total += int(student_score[0]) * 0.75
            elif student_score[1] == 3:
                total += int(student_score[0]) * 0.5
            else:
                total += 0
        average = total / len(score)
        output.append(average)
    return output

scores = [[(90,0),(80,1),(70,2),(60,3),(50,4)],[(100,10),(90,0),(80,0),(90,0)],[(0,0),(20,0),(40,1),(100,0),(100,0),(100,0)]]
print(average_scores(scores))        