# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def get_names (first_names, last_names):
    full_names=[]
    for first in first_names:
        for last in last_names:
            full= first + ' ' +last
            full_names.append(full)
    return full_names

def average_scores (grades):
    averages=[]
    for student in grades:
        totalscore=0
        for assignment in student:
            if assignment[1]==0.0:
                score = assignment[0]
            elif assignment[1]==1.0:
                score=assignment[0]*0.9
            elif assignment[1]==2:
                score =assignment[0]*0.75
            elif assignment[1]==3:
                score=assignment[0]*0.50
            elif assignment[1]>=4:
                score=0
            totalscore+=score
        studentaverage=totalscore/len(student)
        averages.append(studentaverage)
    return averages

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]


print(average_scores(scores))