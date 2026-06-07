# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for names in first_names:
        for more_names in last_names:
            full_names.append(names + " " + more_names)
    return full_names

#first_names = ['Ari', 'Taylor']
#last_names = ['Levine', 'Lopez', 'Khan', 'Wang']

#print(get_names(first_names, last_names))

def average_scores(lst):
    averages = []
    for students in lst:
        average = 0.0
        num_assignments = 0
        for assignments in students:
            #print(assignments[0], assignments[1])
            num_assignments += 1
            if assignments[1] == 0:
                average += assignments[0]
            elif assignments[1] == 1:
                average += assignments[0] * .90
            elif assignments[1] == 2:
                average += assignments[0] * .75
            elif assignments[1] == 3:
                average += assignments[0] * .50
            else:
                average += assignments[0] * 0
        averages.append(average / num_assignments)
    return(averages)

#scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
#          [(100, 10), (90, 0), (80, 0), (90, 0)], 
#          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
#print(average_scores(scores))

