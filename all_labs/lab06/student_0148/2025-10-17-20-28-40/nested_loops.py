# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(fname, lname):
    full_names = []
    for first in fname:
        for last in lname:
            full_names.append(first + " " + last)
    
    return full_names

def average_scores(lists):
    averages = []
   
    for score in lists:
        count = 0
        for l in score:
            if l[1] == 0:
                count+=l[0]
            elif l[1] == 1:
                count+=l[0]*.9
            elif l[1] == 2:
                count+=l[0]*.75
            elif l[1] == 3:
                count+=l[0]*.5
            else:
                count+=0
        averages.append(count/len(score))

    return averages

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(scores))


