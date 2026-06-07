
# Authors   : REDACTED
# Emails    : REDACTED
# Spire ID REDACTED

def get_names(fn, ln):
    full_names=[]
    for i in fn:
        for j in ln:
            full_names.append(f'{i+' '+j}')
    return full_names

first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']

print(get_names(first_names, last_names))

def average_scores(list):
    average_list=[]
    average=0
    for i in list:
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

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(scores))