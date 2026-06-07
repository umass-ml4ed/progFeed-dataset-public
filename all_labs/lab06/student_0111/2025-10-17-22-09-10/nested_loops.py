# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names,last_names):
    ind=0
    full_names=[]
    for i in first_names:
        for n in last_names:
            full_names.append(i+" "+n)
    return full_names
print (get_names(['Ari', 'Taylor'],['Levine', 'Lopez', 'Khan', 'Wang']))


def average_scores(lisoflis):
    finallis=[]
    for lis in lisoflis:
        total=0
        for i in lis:
            if i[1]==0:
                grade=i[0]*1
            elif i[1]==1:
                grade=i[0]*0.9
            elif i[1]==2:
                grade=i[0]*0.75
            elif i[1]==3:
                grade=i[0]*0.50
            elif i[1]>=4:
                grade=0
            total+=grade
        aver=total/len(lis)
        finallis.append(aver)
    return finallis
print(average_scores([[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]))


            
