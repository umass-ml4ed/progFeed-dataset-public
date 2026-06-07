# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    full_names = [] 
    for firstname in first_names:
        for lastname in last_names:
            full_names.append(firstname + " " + lastname)
    return full_names

def average_scores(scores):
    averages = []
    for list in scores:
        total = 0
        for grade, late in list:
            if late == 0:
                total += grade
            if late == 1:
                total += grade *.9
            if late == 2:
                total += grade *.75
            if late == 3:
                total += grade *.5
            if late >= 4:
                total += grade *0
        averages.append(total / len(list))
    return averages
            
            

   



        
        
    



