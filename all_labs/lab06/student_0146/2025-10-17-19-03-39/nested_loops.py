# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for i in first_names:
        for j in last_names:
            full_names.append(f'{i} {j}')
    return full_names

def average_scores(list):
    avg_grades = []
    for l in list:
        grades = 0
        for t in l:
            if t[1] == 0:
                grades += (t[0])
            elif t[1] == 1:
                grades += (0.9 * t[0])
            elif t[1] == 2:
                grades += (0.75 * t[0])
            elif t[1] == 3:
                grades += (0.5 * t[0])
            elif t[1] >= 4:
                grades += (0)
        avg_grades.append(grades / len(l))
    return avg_grades
                
