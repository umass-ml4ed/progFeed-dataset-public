# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def get_names(first_names, last_names):
    full_names = []
    for firstname in first_names:
        for lastname in last_names:
            full_names.append(firstname + " " + lastname)
    return full_names

def average_scores(scorelists):
    average_scores = []
    
    for list in scorelists:
        score_total = 0
        for score in list:
            if score[1] >= 4:
                x=0
            elif score[1] >= 3:
                x=0.5
            elif score[1] >= 2:
                x=0.75
            elif score[1] >=1:
                x=0.9
            else:
                x=1
            score_total = score_total + score[0]*x
        average = score_total/len(list)
        average_scores.append(average)
    return average_scores




            



