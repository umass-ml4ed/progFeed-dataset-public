# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def get_names(first_names,last_names):
    full_names=[]
    for first in first_names:
        for last in last_names:
            full_names.append(first+" "+last)
    return full_names

def average_scores(scores):
    averages=[]
    for lst in scores:
        n=0
        total=0
        for score in lst:
            if score[1]==0:
                total+=score[0]
            elif score[1]==1:
                total+=score[0]*0.9
            elif score[1]==2:
                total+=score[0]*0.75
            elif score[1]==3:
                total+=score[0]*0.5
            n+=1
        averages.append(total/n)
    return averages