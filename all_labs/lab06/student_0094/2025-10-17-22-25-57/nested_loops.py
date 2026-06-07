# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

first_names = ['Ari', 'Taylor']
last_names  = ['Levine', 'Lopez', 'Khan', 'Wang']

full_names = []                      
def get_names(first_names, last_names):
    for first_name in first_names:             
        for last_name in last_names:          
            full_name = f"{first_name} {last_name},"
            full_names.append(full_name)    
            print(full_name, end=' ')       
            
        
print(get_names(first_names, last_names))
                          





def average_scores(all_students):

    def credit(late):
        if late == 0:  return 1.00
        if late == 1:  return 0.90
        if late == 2:  return 0.75
        if late == 3:  return 0.50
        return 0.00  

    avgs = []
    for assignments in all_students:
        adjusted_total = 0.0
        for grade, late in assignments:
            adjusted_total += grade * credit(late)
        avgs.append(adjusted_total / len(assignments) if assignments else 0.0)
    return avgs

all_students = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]   
print(average_scores(all_students))