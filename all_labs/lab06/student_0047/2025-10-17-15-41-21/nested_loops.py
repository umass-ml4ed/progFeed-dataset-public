# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names=[]
    for fname in first_names:
        for lname in last_names:
            full_names.append(fname+" "+lname)
    return full_names

def average_scores(scores):
    average_list=[]
    average=0
    for i in range(0, len(scores)):
        sum=0
        for grade in scores[i]:
            if grade[1]==0:
                sum+=grade[0]
            elif grade[1]==1:
                sum+=grade[0]*.9
            elif grade[1]==2:
                sum+=grade[0]*.75
            elif grade[1]==3:
                sum+=grade[0]*.5
            else:
                sum+=0
        average=sum/len(scores[i])
        average_list.append(average)
    return average_list
        
scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(scores))


            


