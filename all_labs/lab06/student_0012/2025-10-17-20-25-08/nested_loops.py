# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
score_test = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]

def get_names(first, last):
    names = []
    for f in first:
        for l in last:
            names.append(f + " " + l)
    return names

def average_scores(scores):
    averages = []
    for student_scores in scores:
        total_score = 0
        count = len(student_scores)
        for score, weight in student_scores:
            net_score = 0
            if weight == 0:
                net_score = score
            elif weight == 1:
                net_score = score * 0.9
            elif weight == 2:
                net_score = score * 0.75
            elif weight == 3:
                net_score = score * 0.5
            elif weight >= 4:
                net_score = 0
            total_score += net_score
        average = total_score / count
        averages.append(average)
    return averages

print(average_scores(score_test))

