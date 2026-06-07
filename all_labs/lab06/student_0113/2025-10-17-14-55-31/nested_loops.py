#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def get_names(first_names, last_names):
    full_names = []
    for i in range(len(first_names)):
        for j in range(len(last_names)):
            full = first_names[i] + " " + last_names[j]
            full_names.append(full)
    return full_names

first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']

print(get_names(first_names, last_names))

def average_scores(scores):
    penalties = {0: 1, 1: 0.9, 2: 0.75, 3: 0.5}
    average = []
    for student in scores:
        total = 0
        for grade, lateness in student:
            if lateness >= 4:
                penalty = 0
            else:
                penalty = penalties[lateness]
            total += grade * penalty
        average.append(total / len(student))
    return average


scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(scores))

