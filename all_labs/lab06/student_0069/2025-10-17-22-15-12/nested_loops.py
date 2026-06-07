# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def get_names(first_name, last_names):
    
    full_name = []

    for i in first_name:
        for s in last_names:
            full_name.append(f"{i} {s},")

    return full_name 


def average_scores(scores):
  
   
    penalties = {0: 1.0, 1: 0.9, 2: 0.75, 3: 0.5}
    
    averages = [] 
    
    for student in scores:
        total = 0
        for grade, lateness in student:
           
            if lateness >= 4:
                penalty = 0
            else:
                penalty = penalties[lateness]
            
            total += grade * penalty
        
       
        avg = total / len(student)
        averages.append(avg)
    
    return averages