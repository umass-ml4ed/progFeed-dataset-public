# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names=[]
    for f in first_names:
        for l in last_names:
            full_names.append(f"{f} {l}")
    return full_names

#print(get_names(['Ari', 'Taylor'], ['Levine', 'Lopez', 'Khan', 'Wang']))

def average_scores(lis):
    new_lst = []
    for l in lis:
        score = 0
        for i in l:
            penalty = 1
            if i[1] == 1:
                penalty = 0.9
            if i[1] == 2:
                penalty = 0.75
            if i[1] == 3:
                penalty = 0.5
            if i[1] >= 4:
                penalty = 0
            score =score + i[0] * penalty
        avg_score = score / len(l)
        new_lst.append(avg_score)
    return new_lst
            

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(scores))

