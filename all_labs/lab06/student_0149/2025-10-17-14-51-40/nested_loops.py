# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names (first_names2,last_names):
    full_names = []
    for i in first_names2:
        for i1 in last_names:
            full_names.append(i + " " + i1)
    return full_names

def average_scores (list):
    to_output = []
    for i in list:
        score_sum = 0
        print(range(len(i)))
        for thing in range(len(i)):
        #for thing in i:
            if i[thing][1] == 0:
                score_sum += i[thing][0]
            if i[thing][1] == 1:
                score_sum += (i[thing][0] * .9)
            if i[thing][1] == 2:
                score_sum += (i[thing][0] * .75)
            if i[thing][1] == 3:
                score_sum += (i[thing][0] * .5)
        to_output.append(score_sum/len(i))
    return to_output
first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
#print(get_names(first_names,last_names))

listy = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(listy))