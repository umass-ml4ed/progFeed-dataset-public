# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def get_names(first_names, last_names):
    full_names =[]
    for i in first_names:
        for g in last_names:
            new_name = i + " " + g
            full_names.append(new_name)
    return full_names

def average_scores(scores):
    final_scores = []
    for student in scores:
        total = 0
        average_score = 0
        for g in student:
            if(g[1] == 1):
                total += g[0] * 0.9
            elif(g[1] == 2):
                total += g[0] * 0.75
            elif(g[1] == 3):
                total += g[0] * 0.50
            elif(g[1] >= 4):
                total += g[0] * 0
            else:
                total += g[0]
        average_score = total / len(student)
        final_scores.append(average_score)
    return final_scores

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]

print(average_scores(scores))