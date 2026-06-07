# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names: list, last_names: list):
    full_names=[]

    for i in first_names:
        for j in last_names:
            name_combo = i + ' ' + j
            full_names.append(name_combo)
    return full_names


def average_scores(scores):
    penalties = {
        0: 1.00,
        1: 0.90,
        2: 0.75,
        3: 0.50
        }
    result = []
    for student in scores:
        total = 0
        for grade, lateness in student:
            if lateness >= 4:
                final = 0
            else:
                final = grade * penalties.get(lateness, 0)
            total += final
        average = total / len(student)
        result.append(average)
    
    return result  


