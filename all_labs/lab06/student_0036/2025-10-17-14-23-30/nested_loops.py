# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first:list,last:list):
    full_names=[]
    for i in first:
        for j in last:
            full_names.append(i+" "+j)
    return full_names

first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']

print(get_names(first_names,last_names))


def average_scores(scores:list):
    all_averages=[]
    for students in scores:
        grades=0
        total=len(students)
        for grade, late in students:
            if late == 0:
                penalty=1.0
            if late ==1:
                penalty=.9
            if late ==2:
                penalty=.75
            if late ==3:
                penalty=.5
            if late >=4:
                penalty=0
            grades+=grade*penalty
        all_averages.append(grades/total)
    return all_averages

scores=[[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]

print(average_scores(scores))