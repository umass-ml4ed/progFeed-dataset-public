# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for a in first_names:
        for b in last_names:
            full_name = a + " " + b
            full_names.append(full_name)
    return full_names


def average_scores(scores):
    averages = []
    for i in scores:
        total = 0
        for grade, late in i:
            if late == 0:
                penalty = 1.0
            elif late == 1:
                penalty = 0.9
            elif late == 2:
                penalty = 0.75
            elif late == 3:
                penalty = 0.5
            else:
                penalty = 0.0
            total += grade * penalty
        average = total/len(i)
        averages.append(average)
    return averages

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(scores))