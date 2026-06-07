# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for i in range(len(first_names)):
        for j in range(len(last_names)):
            full_names.append((first_names[i] + " " + last_names[j]))
    return full_names

def average_scores(scores):
    averages = []
    for i in scores:
        total = 0.0
        null = 0
        for j in i:
            grade = j[0]
            lateness = j[1]
            if lateness == 0:
                credit = 1.0
            elif lateness == 1:
                credit = 0.9 
            elif lateness == 2:
                credit = 0.75
            elif lateness == 3:
                credit = 0.5
            else:
                credit = 0.0
            new_grade = grade * credit
            total += new_grade
            null += 1
        if null == 0:
            averages.append(0.0)
        else:
            new_average = total/null
            averages.append(new_average)
    return averages




