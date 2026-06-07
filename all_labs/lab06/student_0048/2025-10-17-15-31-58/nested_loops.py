# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def get_names(first_names, last_names):
    full_names = []
    for i in first_names:
        for j in last_names:
            full_names.append(i+' '+j)
    return full_names 

def average_scores(scores):
    curr_score = []
    for i in scores:
        total = 0
        for j in i:
            if j[1] == 0:
                grade = j[0]*1.00
            if j[1] == 1:
                grade = j[0]*.90
            if j[1] == 2: 
                grade = j[0]*.75
            if j[1] == 3: 
                grade = j[0]*.50
            if j[1] >= 4: 
                grade = j[0]*0
            total += grade 
        average = total/len(i)
        curr_score.append(average)
    return curr_score

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(scores))


