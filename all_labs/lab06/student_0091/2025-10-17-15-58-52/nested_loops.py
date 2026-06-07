# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']


def get_names(first_names, last_names):
    full_names = []
    for firstName in first_names:
        for lastName in last_names:
            full_name = firstName + " " + lastName
            full_names.append(full_name)

    return full_names

print(get_names(first_names,last_names))

scores =[[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)],
         [(100, 10), (90, 0), (80, 0), (90, 0)],
         [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]
         ]


def average_scores(scores):
    averages = []

    for student in scores:
        total = 0
        for grade, lateness in student:
            if lateness == 0:
                penalty = 1
            elif lateness == 1:
                penalty = 0.9
            elif lateness == 2:
                penalty = 0.75
            elif lateness == 3:
                penalty = 0.5
            else:
                penalty = 0
            total += grade * penalty
        averages.append(total / len(student))

    return averages
print(average_scores(scores))