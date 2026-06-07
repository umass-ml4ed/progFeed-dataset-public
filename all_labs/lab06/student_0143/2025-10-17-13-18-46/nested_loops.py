# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']

def get_names(first:list,Last:list):
    List = []
    for first in first_names:
        for last in last_names:
            List.append(first + ' ' + last)
    return List

def average_scores(Lists_of_scores:list):
    penalties = {0:1,1:.9,2:.75,3:.5}
    Averaged_scores =[]
    for list_of_scores in Lists_of_scores:
        sum_of_scores = 0
        for score in list_of_scores:
            if score[1] > 3:
                continue
            sum_of_scores += score[0] * penalties[score[1]]
        Averaged_scores.append(sum_of_scores / len(list_of_scores))
    return Averaged_scores

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)],
          [(100, 10), (90, 0), (80, 0), (90, 0)],
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(scores))