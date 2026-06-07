# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def get_names(first_names: list, ast_names: list) ->  list:
    
    full_names=[]
    
    for first in first_names:

        for last in last_names:

            fullname = first + " " + last

            full_names.append(fullname)
    
    return full_names


def average_scores(scores: list)  -> list:
    avg_scores = []
    for student in scores:
        total_score = 0
        for scores in student:

            if scores[1] == 0:
                score = scores[0]
                total_score += score
            elif scores[1] == 1:
                score = scores[0] * 0.9
                total_score += score
            elif scores[1] == 2:
                score = scores[0] * 0.75
                total_score += score
            elif scores[1] == 3:
                score = scores[0] * 0.5
                total_score += score
            elif scores[1] >= 4:
                score = 0
                total_score += score
        avgscore = total_score / len(student)
        avg_scores.append(avgscore)
    return avg_scores
    

            









