# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
def get_names(first_name,last_name):
    new_list=[]
    for i in range (len(first_name)):
        for j in range (len(last_name)):
            name = first_name[i] +" " +last_name[j]
            new_list.append(name)
    return new_list
# first_names = ['Ari', 'Taylor']
# last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
# print (get_names(first_names,last_names))
# score ->tuple
def score_after_pen(score):
    if (score[1]==0):
        new_score = score[0]
    elif (score[1] == 1):
        new_score = score[0]*90/100
    elif (score[1] == 2):
        new_score = score[0]*75/100
    elif (score[1] ==3):
        new_score = score[0]*50/100
    else:
        new_score = 0
    return new_score
def average_scores(lst):
    avg_score =[]
    for i in range (len(lst)):
        count = 0
        total = 0 
        for score_tuple in lst[i]:
            total = total + score_after_pen(score_tuple)
            count = count + 1
        avg_score.append(total/count)
    return avg_score

# scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
#           [(100, 10), (90, 0), (80, 0), (90, 0)], 
#           [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
# print(average_scores(scores))