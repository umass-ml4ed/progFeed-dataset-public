# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(lst1, lst2):
    names_list = []
    for i in lst1:
        for j in lst2:
            full_name = i + " " + j
            names_list.append(full_name)
    return names_list

def average_scores(scores):
    lateness = {
        0: 1,
        1: 0.9,
        2: 0.75,
        3: 0.5,
        }
    
    averages = []

    for i in scores:
        total_score = 0
        for j in i:
            if j[1] >= 4: continue
            total_score += (j[0] * lateness[j[1]])
        averages.append(total_score/len(i))
    return averages

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]

print(average_scores(scores))
