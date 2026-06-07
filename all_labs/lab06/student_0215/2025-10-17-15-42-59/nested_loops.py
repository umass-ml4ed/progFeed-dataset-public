# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def get_names(first_names,last_names):
    full_names = []
    for i in range(len(first_names)):
        full = first_names[i] + " " + last_names[i]
        full_names.append(full)
    return full_names

def average_scores(parameter):
    after = []
    for student_scores in parameter:
        for item in student_scores:
            grade = item[0]
            lateness = item[1]
  
            if lateness == 0:
                grade1 = grade
                after.append(grade1)
            elif lateness == 1:
                grade2 = grade * 0.9
                after.append(grade2)
            elif lateness == 2:
                grade3 = grade * 0.75
                after.append(grade3)
            elif lateness == 3:
                grade4 = grade * 0.5
                after.append(grade4)
            else:
                grade5 = grade * 0
                after.append(grade5)
    return after
                
