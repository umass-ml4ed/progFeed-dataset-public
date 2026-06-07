# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def get_names(first_names: str, last_names: str):
    full_names = []
    for first in first_names: 
        for last in last_names: 
            full_names.append(first + ' ' + last)
    return full_names 

first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']

print(get_names(first_names, last_names))

#-----------------------------

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]


def average_scores(scores: tuple):
    averages = [0, 0, 0]
    x = 0
    #averages1 = []
    #averages2 = []
    #averages3 = []
    while x <= 2:
        for student in scores:
          
            for grade in student:
                
                if grade[1] == 0: 
                    averages[x] += grade[0]
                elif grade[1] == 1:
                    averages[x] += (grade[0]*.9)
                elif grade[1] == 2:
                    averages[x] += (grade[0]*.75)
                elif grade[1] == 3:
                    averages[x] += (grade[0]*.50)
                else: 
                    averages[x] += (grade[0]*0)
                #elif grade[1] <= 4:
                #   averages[x] += grade[0]*0
            
            averages[x] = (averages[x] / len(student))
        
            x += 1

    return averages

print(average_scores(scores))



