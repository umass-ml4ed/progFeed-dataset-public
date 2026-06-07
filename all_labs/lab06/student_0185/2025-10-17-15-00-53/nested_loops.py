# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(f: list, l: list):
    full_names = []
    for i in range(len(f)):
        for j in range(len(l)):
            full_names.append(f[i] + " " + l[j])
    return full_names

def average_scores(l: list):
    average_grade = []
    for i in l:
        n = 0
        total = 0
        for j in i:
            if j[1] == 0:
                total += j[0]
            if j[1] == 1:
                total += j[0] * 0.9
            if j[1] == 2:
                total += j[0] * 0.75
            if j[1] == 3:
                total += j[0] * 0.5
            if j[1] >= 4:
                total += j[0] * 0
        n += 1
        average_grade.append(total/n)
    return average_grade 
    

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]

print(average_scores(scores))