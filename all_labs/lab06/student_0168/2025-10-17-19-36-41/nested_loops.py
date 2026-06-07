# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
def get_names(first_names, last_names):
    full_names=[]
    for i in range(0, len(first_names)):
        for j in range(0, len(last_names)):
            first_name = first_names[i]
            last_name = last_names[j]
            full_names.append(f"{first_name} {last_name}")
    return full_names
print(get_names(first_names, last_names))

def average_scores(lsts):
    averages=[]
    for i in range(0,len(lsts)):
        lst=lsts[i]
        scores=0
        for j in range(0, len(lst)):
            grade=lst[j][0]
            late=lst[j][1]
            if late==0:
                penalty=1
            if late==1:
                penalty=.9
            if late==2:
                penalty=.75
            if late==3:
                penalty=.5
            if late>=4:
                penalty=0
            score=grade*penalty
            scores=scores+score
            
        average=scores/len(lst)
        averages.append(average)
    return averages

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(scores))


