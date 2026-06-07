# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(f,l):
    full = []
    for i in f:
        for j in l:
            full.append(i+" "+j)
    return full

def average_scores(lst):
    avglst = []
    for i in lst:
        avg = 0
        for j in i:
            if j[1] == 0:
                avg+=j[0]
            elif j[1] == 1:
                avg+=(j[0]*0.9)
            elif j[1] == 2:
                avg+=(j[0]*0.75)
            elif j[1] == 3:
                avg+=(j[0]*0.5)
            elif j[1] == 4:
                avg+=0
        avglst.append((avg/len(i)))
    return avglst


