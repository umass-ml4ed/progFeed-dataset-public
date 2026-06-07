# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(list1,list2):
    full_names=[]
    for i in list1:
        for j in list2:
            full_names.append(i+' '+j)
    return full_names

def average_scores(big_list):
    average=[]
    for student in big_list:
        total=0
        for assignment in student:
            if assignment[1]==0:
                total+=assignment[0]
            elif assignment[1]==1:
                total+=assignment[0]*.9
            elif assignment[1]==2:
                total+=assignment[0]*.75
            elif assignment[1]==3:
                total+=assignment[0]*.5
        average.append(total/len(student))
    return average

print(average_scores([[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
))