# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']

def get_names(first:list, last: list):
    combos = []
    for name in first:
        for surname in last:
            combos.append(f"{name} {surname}")
    return combos

print(get_names(first_names, last_names))

all_scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)],
              [(100, 10), (90, 0), (80, 0), (90, 0)],
              [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]

def average_scores(scores: list): 
    # scores [student] [assignment] [grade (0), late (1)]
    averages = []
    for student in range(len(scores)):
        total = 0.0
        for assignment in range(len(scores[student])):
            if scores[student][assignment][1] == 0:
                total += scores[student][assignment][0]
            elif scores[student][assignment][1] == 1:
                total += (scores[student][assignment][0]*.9)
            elif scores[student][assignment][1] == 2:
                total += (scores[student][assignment][0]*.75)
            elif scores[student][assignment][1] == 3:
                total += (scores[student][assignment][0]*.5)
            # else:
            #     total += 0
        avg = total/len(scores[student])
        averages.append(avg)
    return averages

print(average_scores(all_scores))