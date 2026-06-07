# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
import math
def get_names(Fnames:list, Lnames:list):
    Full_names = []
    for i in Fnames:
        for j in Lnames:
            Full_names.append(f"{i} {j}")
    return (Full_names)

def average_scores(lst:list):
    averages=[]
    for i in lst:
        average_sc_lst=[]
        for (j,k) in i:
            if k>10:
                continue
            elif k == 0:
                average_sc_lst.append(j)
            elif k ==1:
                x90=.9*j
                average_sc_lst.append(x90)
            elif k ==2:
                x75=.75*j
                average_sc_lst.append(x75)
            elif k ==3:
                x5=.5*j
                average_sc_lst.append(x5)
            else:
                average_sc_lst.append(0)
        avg = sum(average_sc_lst) / len(average_sc_lst)
        averages.append(avg)
    return averages
print(average_scores([[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]))