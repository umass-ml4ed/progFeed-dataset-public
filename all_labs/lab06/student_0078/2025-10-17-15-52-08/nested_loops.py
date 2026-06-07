# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def get_names(first_names, last_names):
    full_names = []
    for i in first_names:
        for j in last_names:
            full_names.append(print(f"{i} {j}", end=" "))
    return full_names
    
def average_scores(lis):
    result = []
    for student in lis:
        total = 0
        for assignment in student:
            grade = assignment[0]
            late = assignment[1]
            if late == 0:
                total += grade * 1
            elif late == 1:
                total += grade * 0.9
            elif late == 2:
                total += grade * 0.75
            elif late == 3:
                total += grade * 0.5
            else:
                total += 0
        avg = total / len(student)
        result.append(avg)
    return result


    