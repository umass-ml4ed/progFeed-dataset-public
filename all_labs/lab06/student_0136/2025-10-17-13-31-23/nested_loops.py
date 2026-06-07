# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for i in range(len(first_names)):
        for j in range(len(last_names)):
            name = first_names[i] + " " + last_names[j]
            full_names.append(name)
    return full_names

def average_scores (lst):
    average = 0
    new_lst = []
    for a in range(len(lst)):
        sum = 0
        counter = 0
        for b in range(len(lst[a])):
            if (lst[a][b][1] == 0):
                sum += lst[a][b][0]
            elif (lst[a][b][1] == 1):
                sum += lst[a][b][0] * 0.9
            elif (lst[a][b][1] == 2):
                sum += lst[a][b][0] * 0.75
            elif (lst[a][b][1] == 3):
                sum += lst[a][b][0] * 0.5
            else:
                sum += 0
            counter += 1
        average = sum / counter
        new_lst.append(average)
    return new_lst

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(scores))