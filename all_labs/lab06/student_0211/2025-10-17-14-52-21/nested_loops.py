# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(fList,lList):
    fullList = []
    for i in fList:
        for j in lList:
            fullList.append(i +" " +j)
    return fullList

first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
print(get_names(first_names,last_names))

lst =  [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(lst[0][0][0])

def average_scores(lst: list):
    avg = []
    sum = 0
    for i in range(len(lst)):
        sum = 0
        for j in range(len(lst[i])):
            if lst[i][j][1] == 0:
                sum += lst[i][j][0]
            elif lst[i][j][1] == 1:
                sum += lst[i][j][0] * 0.9
            elif lst[i][j][1] == 2:
                sum += lst[i][j][0] * 0.75
            elif lst[i][j][1] == 3:
                sum += lst[i][j][0] * 0.50
            else:
                sum += lst[i][j][0] * 0
        avg.append(sum/len(lst[i]))
    return avg  
print(average_scores(lst))
         
