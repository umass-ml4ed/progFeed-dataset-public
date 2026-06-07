# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(fnames,lnames):
    names = []
    for f in fnames:
        for l in lnames:
            names.append(f+" "+l)
    return names

#first_names = ['Ari', 'Taylor']
#last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
#print(get_names(first_names,last_names))

def average_scores(stuList):
    gpa = []
    for t in range (len(stuList)):
        sum = 0
        for i in range(len(stuList[t])):
            if stuList[t][i][1] == 0:
                sum += stuList[t][i][0]
            elif stuList[t][i][1] == 1:
                sum += (stuList[t][i][0] * 0.9)
            elif stuList[t][i][1] == 2:
                sum += (stuList[t][i][0] * 0.75)
            elif stuList[t][i][1] == 3:
                sum += (stuList[t][i][0] * 0.5)
        sum /= len(stuList[t])
        gpa.append(sum)
    return gpa

#grades = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
#print(average_scores(grades))