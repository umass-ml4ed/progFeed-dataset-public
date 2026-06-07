# Authors   : REDACTED
# Emails    : REDACTED
# Spire ID REDACTED

def get_names(first_names, surnames):
    full_names=[]
    for i in first_names:
        for j in surnames:
            full_names.append(f'{i+' '+j}')
    return full_names

def average_scores(scores):
    average_list=[]
    average=0
    for i in scores:
        sum=0
        for j in i:
            if j[1]==0:
                sum+=j[0]
            elif j[1] == 1:
                sum += j[0] * 0.9
            elif j[1] == 2:
                sum += j[0] * 0.75
            elif j[1] == 3:
                sum += j[0] * 0.5
            elif j[1] >= 4:
                sum += j[0] * 0
        average=sum/len(i)
        average_list.append(average)
    return average_list