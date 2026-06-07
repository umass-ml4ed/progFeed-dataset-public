# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(given, surnames):
    full_names = []
    for namea in given:
        for nameb in surnames:
            full_names.append(f"{namea} {nameb}")
    return full_names

# first_names = ['Ari', 'Taylor']
# last_names = ['Levine', 'Lopez', 'Khan', 'Wang']

# print(get_names(first_names, last_names))

def average_scores(scores):
    avg = []
    studentscoreplaceholder = 0
    for a in scores:
        for b in a:
            if b[1] == 1:
                studentscoreplaceholder = studentscoreplaceholder + (b[0]*0.9)
            elif b[1] == 2:
                studentscoreplaceholder = studentscoreplaceholder + (b[0]*0.75)
            elif b[1] == 3:
                studentscoreplaceholder = studentscoreplaceholder + (b[0]*0.5)
            elif b[1] == 0:
                studentscoreplaceholder = studentscoreplaceholder + b[0]
            else:
                continue
        avg.append(studentscoreplaceholder/len(a))
        studentscoreplaceholder = 0
    return avg

# scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
#           [(100, 10), (90, 0), (80, 0), (90, 0)], 
#           [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
# print(average_scores(scores))

                