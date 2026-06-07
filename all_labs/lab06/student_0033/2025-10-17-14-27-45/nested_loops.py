# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_name,last_name):
    full_names=[]
    for i in range(len(first_name)):
        first=first_name[i]
        for j in range(len(last_name)):
            last=last_name[j]
            a=first + " " + last
            full_names.append(a)
    return full_names

def average_scores(l):
    averages = []
    for student in l:
        if not student:
            averages.append(0.0)
            continue

        total = 0.0
        count = 0
        for assignment in student:
            grade, lateness = assignment
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
            count += 1

        averages.append(total / count if count else 0.0)

    return averages

