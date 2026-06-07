# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(flst, llst):
    fnames = ""
    full_names=[]
    for name in flst:
        for lname in llst:
            fnames = name + " " + lname
            full_names.append(fnames)
    return full_names

def average_scores(lst):
    averages = []
    for grades in lst:
        total = 0
        count = 0
        for grade, lateness in grades:
            if lateness == 0:
                new_grade = grade
            elif lateness == 1:
                new_grade = grade * 0.9
            elif lateness == 2:
                new_grade = grade * 0.75
            elif lateness == 3:
                new_grade = grade * 0.5
            else:
                new_grade = 0
            total += new_grade
            count += 1
        average = total / count
        averages.append(average)
    return averages

first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
print(get_names(first_names, last_names))

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(scores))