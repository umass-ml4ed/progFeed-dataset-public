# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_name, last_name):
    full_names = []
    for i in first_name:
        for j in last_name:
            full_names.append(i + ' '+j)
    return full_names

def average_scores(scores):
    result = []
    for i in scores: 
        total = 0
        count = 0 
        for j in i:
            grade = j[0]
            lateness = j[1]

            if lateness == 0:
                multiplier = 1
            elif lateness == 1:
                multiplier = 0.9
            elif lateness == 2:
                multiplier = 0.75
            elif lateness == 3:
                multiplier = 0.5
            else: 
                multiplier = 0 

            total += grade * multiplier
            count +=1 

        avg = total/count 
        result.append(avg)

    return result 
            

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(scores))


