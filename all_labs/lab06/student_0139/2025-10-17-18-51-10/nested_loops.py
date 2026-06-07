# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(l1,l2):
    l3=[]
    for i in l1:
        for j in l2:
            l3.append(i+" "+j)
    return l3
# first_names = ['Ari', 'Taylor']
# last_names = ['Levine', 'Lopez', 'Khan', 'Wang']

# print(get_names(first_names,last_names))

def average_scores(l1):
    l2=[]
    a=0
    for i in l1:
        for j in i:
            if j[1]==0:
                a+=j[0]
                print(a)
            elif j[1]==1:
                a+=(j[0]*0.9)
                print(a)
            elif j[1]==2:
                a+=(j[0]*0.75)
                print(a)
            elif j[1]==3:
                a+=(j[0]*0.5)
                print(a)
            elif j[1]>=4:
                a+=(0)
                print(a)
        l2.append(a/len(i))
        print(l2)
        a=0
    return(l2)

# scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
#           [(100, 10), (90, 0), (80, 0), (90, 0)], 
#           [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
# print(average_scores(scores))