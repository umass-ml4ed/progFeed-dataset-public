# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names,last_names):
    full_names = []
    for i in first_names:
        for j in last_names:
                full_names.append(i + ' ' +j)
    return full_names

def average_scores(scores):

    averages = []
    for student in scores:
        if len(student) == 0:
            averages.append(0.0)
            continue

        total = 0.0
        for grade, lateness in student:
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

            total += grade * credit

        avg = total / len(student)
        averages.append(avg)

    return averages
                        
