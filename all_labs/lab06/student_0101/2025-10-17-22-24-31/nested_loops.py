# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names=[]
    for first in first_names:
        for last in last_names:
            x= (first + " " +last)
            full_names.append(x)
    return full_names
def average_scores(scores):
    averages=[]
    pterodactyl ={0:1, 1:.9, 2:.75, 3:.5, 4:0}
    for tuple in scores:
        p=0
        d=0
        for amount in tuple:
            p += amount[0]* pterodactyl[amount[1]]
            d=+1
        l=p/d
        averages.append(l)
    return averages
print(average_scores([[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]))             
            
                
                
