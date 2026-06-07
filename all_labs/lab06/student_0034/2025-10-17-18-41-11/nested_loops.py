# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(lst1, lst2):
    full_names = []
    for name in lst1:
        for surname in lst2:
            whole = (str(name)+' '+str(surname))
            full_names.append(whole)
    return full_names

def average_scores(lsts):
    grades = []
    for student in lsts:
        total_scores = 0.0
        for grade in student:
            if grade[1] == 0:
                total_scores += float(grade[0])
            elif grade[1] == 1:
                total_scores += float(grade[0]) * 0.9
            elif grade[1] == 2:
                total_scores += float(grade[0]) * 0.75
            elif grade[1] == 3:
                total_scores += float(grade[0]) * 0.5
            elif grade[1] >= 4:
                total_scores += 0.0
        grades.append(total_scores / len(student))
    return grades
    