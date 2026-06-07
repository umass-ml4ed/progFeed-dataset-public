# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
full_names = []

def get_names(a, b):
    c = 0
    d = 0
    half_names = []
    for name in a:
        for last in b:
            half_names.append(name + ' ' + last)
    return half_names

print(get_names(first_names, last_names))

# print(wow(first_names, last_names))


# SCORES

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
#student1 = [(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)]
#asnmnt1 = (90, 0)

#func to get penalties
def penalty(a, b):
    if b == 0:
        return a
    elif b == 1:
        return (a * 0.9)
    elif b == 2:
        return (a * 0.75)
    elif b == 3:
        return (a * 0.5)
    else:
        return 0

# func to make weighted scores a list
def score_list(a):
    score_lst = []
    b = 0
    for score in a:
        score_lst.append(penalty(score[0], score[1]))
    return score_lst

# func to find average weighted score per student
def ave_stu(b):
    total = 0
    c = 0
    while (c+1) <= len(b):
        total += float(b[c])
        c += 1
    return total/(len(b))

# final func
def average_scores(scores):
    final_score_list = []
    for student in scores:
        final_score_list.append(ave_stu(score_list(student)))
    return final_score_list

#print(average_scores(scores))

