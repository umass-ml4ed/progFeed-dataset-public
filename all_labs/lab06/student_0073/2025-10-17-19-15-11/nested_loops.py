# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names,last_names):
    full_names=[]
    for i in first_names:                 # outer loop iterates over [1, 9]
        for j in last_names:               # inner loop iterates over [1, 9]
            full_names.append(f'{i} {j}')
    return full_names                              # print a new line

first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']

print(get_names(first_names,last_names))

def average_scores(scores):
    penalties = {0: 1.0, 1: 0.9, 2: 0.75, 3: 0.5}

    averages = []  
    for student in scores:
        total = 0
        for grade, lateness in student:
            multiplier = penalties.get(lateness, 0)
            total += grade * multiplier
        avg = total / len(student)
        averages.append(avg)

    return averages


scores = [
    [(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)],
    [(100, 10), (90, 0), (80, 0), (90, 0)],
    [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]
]

