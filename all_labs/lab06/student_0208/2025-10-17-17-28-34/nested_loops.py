# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(fisrt_names, last_names):
    full_names=[]
    for first in fisrt_names:
        for last in last_names:
            full_names.append(first+' '+last)
    return full_names

print(get_names(['Ari', 'Taylor'], ['Levine', 'Lopez', 'Khan', 'Wang']))

def average_scores(score_lists):
    average_scores=[]
    for scores in score_lists:
        total=0
        for grade, late in scores:
            if late==0:
                total+= grade
            elif late==1:
                total+= grade*0.9
            elif late==2:
                total+= grade*0.75
            elif late==3:
                total+=grade*0.5
            else:
                total+=0
        average_scores.append(total/len(scores))
    return average_scores
            
score_lists=[[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(score_lists))