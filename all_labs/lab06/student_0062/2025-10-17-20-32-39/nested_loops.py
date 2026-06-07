# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for fname in first_names:
        for lname in last_names:
            full_names.append(fname + ' ' + lname)
    return full_names

def average_scores(student_list):
    scores = []
    for student in student_list:
        score_total = 0
        for score in student:
            if score[1] == 0:
                score_total += score[0]
            elif score[1] == 1:
                score_total += score[0] * 0.9
            elif score[1] == 2:
                score_total += score[0] * 0.75
            elif score[1] == 3:
                score_total += score[0] * 0.5
            else:
                continue
        scores.append(score_total/len(student))
    return(scores)