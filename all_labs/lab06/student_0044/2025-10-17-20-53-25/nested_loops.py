# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

#first_names = ['Ari', 'Taylor']
#last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
def get_names(first_names, last_names):
    full_names=[]
    for first in first_names:
        for last in last_names:
            full_names.append(first+' '+last)
    return(full_names)
#print(get_names(['Ari', 'Taylor'], ['Levine', 'Lopez', 'Khan', 'Wang']))

#scores=[[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
def average_scores(scores):
    average=[]
    for a in scores:
        z=0    
        for b, c in a:
            x=b
            if c==0:
                y=x*1
            elif c==1:
                y=x*0.9
            elif c==2:
                y=x*0.75
            elif c==3:
                y=x*0.5
            elif c>=4:
                y=x*0
            z+=y
        t=z/len(a)
        average.append(t)
    return(average)
#print(average_scores([[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)],[(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]))