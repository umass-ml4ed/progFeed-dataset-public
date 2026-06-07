# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for i in first_names:
        for j in last_names:
            a = i + ' ' + j
            full_names.append(a)
    return full_names


def average_scores(scores):
    avg_scores = []
    for i in scores:
        total = 0
        for j in i:
            a = j[0]
            b = j[1]
            if b == 0:
                total += a   
            if b == 1:
                total += (a * 0.90) 
            if b == 2:
                total += (a * 0.75)
            if b == 3:
                total += (a * 0.50) 
            if b >= 4:
                total += 0 
        avg = total / len(i)
        avg_scores.append(avg)
    return avg_scores

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(scores))

