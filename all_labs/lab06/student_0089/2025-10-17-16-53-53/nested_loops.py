# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for i in range(0, len(first_names)):
        for j in range(0, len(last_names)):
            full_names.append(str(first_names[i]) + " " + str(last_names[j])) # i only index. # first_names[i] = values
    return full_names

first_name = ['Ari', 'Taylor']
last_name = ['Levine', 'Lopez', 'Khan', 'Wang']

print(get_names(first_name, last_name))

def average_scores(scores):
    grade = []
    total_score = 0
    for i in scores: #looping through the first set of lists
        total_score = 0 # Making sure the total score resets everytime as i goes to a new list
        for tuple in i: #looping through each tuple
                raw_score = tuple[0] # First score
                penalty = tuple[1] # Checking for any late penalty
                if penalty == 0:
                     total_score += raw_score
                elif penalty == 1:
                     raw_score = raw_score * 0.9
                     total_score += raw_score
                elif penalty == 2:
                     raw_score = raw_score * 0.75
                     total_score += raw_score
                elif penalty == 3:
                     raw_score = raw_score * 0.5
                     total_score += raw_score
                else:
                     total_score += raw_score * 0
        grade.append(total_score / len(i))
    return grade

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]

print(average_scores(scores))
    
