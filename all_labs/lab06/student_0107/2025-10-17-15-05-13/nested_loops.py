# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def get_names(first, last):
    full_names = []
    space = " "
    for i in range(len(first)):
        for j in range(len(last)):
            new = first[i] + space +  last[j]
            full_names.append(new)
    return full_names



first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']


#print(get_names(first_names,last_names))

def average_scores(scores):
    
    average = [ ]
    for i in range(len(scores)):
        element = list(scores[i])
        #print(element)
        grade = 0
        for j in range(len(element)):
            percentage = 0
            l = [scores[i][j]]
            if l[0][1] == 0:
                percentage = 1
            if l[0][1] == 1:
                percentage = 0.9
            if l[0][1] == 2:
                percentage = .75
            if l[0][1] == 3:
                percentage = 0.5
            if l[0][1] >= 4:
                percentage = 0
            grade += l[0][0] * percentage
        grade = grade/len(element)
        average.append(grade)
        





    return average 

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]

print(average_scores(scores))
