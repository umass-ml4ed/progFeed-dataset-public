# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

#1. 
def get_names(first_names,last_names):
    full_names=[]

    for first_name in first_names:
        for last_name in last_names:
            full_name = first_name + " " + last_name
            full_names.append(full_name)
    
    return full_names



# #2.
# (90,0) gr[0]=90 gr[1]=0
# dict={key: value} dict[key]

def average_scores(scores):
    penalty_rates = {
        0: 1.0,    
        1: 0.9,    
        2: 0.75,   
        3: 0.5,         
    }

    average=[]

    for student in scores:
        grade=0  
    
        for gr in student:
            if gr[1]>= 4:
                grade+=gr[0]*0.0
            else:
                grade+=gr[0]*penalty_rates[gr[1]] 

        avg=grade/len(student)
        average.append(avg)
    return average


scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(scores))









