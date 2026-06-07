# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def get_names(first_names,last_names):
    full_names=[]
    for i in first_names:
        name=''
        for j in last_names:
            name=i+' '+j
            full_names.append(name)
    return full_names

def average_scores(L):
    avg_scores=[]
    for scores in L:
        total=0
        for sub_score in scores:
            marks=sub_score[0]
            if sub_score[1]==1:
                marks*=0.9
            elif sub_score[1]==2:
                marks*=0.75
            elif sub_score[1]==3:
                marks*=0.5
            elif sub_score[1]>=4:
                marks*=0
            total+=marks
        avg=total/len(scores)
        avg_scores.append(avg)
    return avg_scores

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(scores))