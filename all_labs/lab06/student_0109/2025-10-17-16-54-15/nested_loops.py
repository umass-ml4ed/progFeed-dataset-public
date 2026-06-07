#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def get_names(fn,ln):
    full_names = []
    for i in fn:
        for j in ln:
            full_names.append(f'{i} {j}')
    return full_names

def average_scores(lst):
    averages = []
    for student in lst:
        raw_sum = 0
        for assignment in student:
                if assignment[1] == 0:
                    raw_sum += assignment[0]
                if assignment[1] == 1:
                    raw_sum += 0.9 * assignment[0]
                if assignment[1] == 2:
                    raw_sum += 0.75 * assignment[0]
                if assignment[1] == 3:
                    raw_sum += 0.5 * assignment[0]
                if assignment[1] >= 4:
                    raw_sum += 0
        averages.append(raw_sum / len(student))
    return averages

lst = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(lst))