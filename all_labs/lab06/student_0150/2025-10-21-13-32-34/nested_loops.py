# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names,last_names):
    full_names = []
    for name1 in first_names:
        for name2 in last_names:
            full_names.append(name1 + " " + name2)
    return full_names

def average_scores(grades):
    list_avg = []
    for student in grades:
        avg = 0
        for assignment in student:
            if assignment[1] == 0:
                avg += int(assignment[0])
            elif assignment[1] == 1:
                avg += int(assignment[0])*.9
            elif assignment[1] == 2:
                avg += int(assignment[0])*.75
            elif assignment[1] == 3:
                avg += int(assignment[0])*.5
            else:
                avg += 0    
        list_avg.append(avg/len(student))
    return list_avg



