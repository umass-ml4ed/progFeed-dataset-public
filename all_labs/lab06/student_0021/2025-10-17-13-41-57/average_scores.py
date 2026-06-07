# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)],
    [(100, 10), (90, 0), (80, 0), (90, 0)],
    [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]

def func1():
    average_scores = [] 
    for i in range(len(scores)):
        count = len(scores[i])
        multiplier = 0 
        total = 0
        for x in range(count):
            if scores[i][x][1] == 0:
                multiplier = 1
            elif scores[i][x][1] == 1:
                multiplier = 0.9 
            elif scores[i][x][1] == 2: 
                multiplier = 0.75 
            elif scores[i][x][1] == 3: 
                multiplier = 0.5 
            else: 
                multiplier = 0
            n = scores[i][x][0]
            total += n * multiplier 
        average = total / count 
        average_scores.append(average)
    return (average_scores)

print(func1())
