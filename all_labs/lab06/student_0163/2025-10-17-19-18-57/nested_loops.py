# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names,last_names):
    full_names=[]
    for i in first_names:
        for j in last_names:
            full_names.append(i+" "+j)
    return full_names

def average_scores(scores):
    newl=[]
    for i in range(len(scores)):
        total=0
        for score, late in (scores[i]):
            if late==0:
                percent=1
            elif late==1:
                percent=0.9
            elif late==2:
                percent= 0.75
            elif late==3:
                percent=0.5
            else:
                percent=0
            marks=score*percent
            total+=marks
        average=total/len(scores[i])
        newl.append(average)
        return newl