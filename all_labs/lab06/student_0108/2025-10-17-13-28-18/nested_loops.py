# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names=[]
    for first in first_names:
        for last in last_names:
            full_names.append(first + " " + last)
    return full_names

first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
print(get_names(first_names, last_names))

def average_scores(student_grades):
    avg_grades=[]
    sum=0
    for grades in student_grades:
        for score in grades:
            if(score[1]==0):
                lateness=1
            elif(score[1]==1):
                lateness=0.9
            elif(score[1]==2):
                lateness=0.75
            elif(score[1]==3):
                lateness=0.5
            else:
                lateness=0
            sum+=score[0]*lateness
            print(sum)
        avg_grades.append(sum/len(grades))
        sum=0
    return avg_grades

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(scores))