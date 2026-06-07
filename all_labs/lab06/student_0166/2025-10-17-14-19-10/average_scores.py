# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def average_scores(scores):
    results = []
    for total_scores in scores:
        t = 0
        for i in total_scores:
            scores = i[0]
            penalty = i[1]
            if penalty==0:
                t = t + scores*1
            elif penalty==1:
                t = t + scores*0.9
            elif penalty==2:
                t = t + scores*0.75
            elif penalty==3:
                t = t + scores*0.5
            else:
                t = t + scores*0
        amount = len(total_scores)
        final_score = t/amount
        results.append(final_score)
    return results

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(scores))

        