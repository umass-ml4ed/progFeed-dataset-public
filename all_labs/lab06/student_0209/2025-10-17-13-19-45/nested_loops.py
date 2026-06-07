# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names:list, last_names:list):
    full_names = []
    for i in first_names:
        for u in last_names:
            full_names.append(i + " " + u)       
    return full_names

def average_scores(lst):
    first_student = lst[0]
    second_student =lst[1]
    third_student = lst[2]
    average_1=[]
    average_2=[]
    average_3=[]
    for grade in first_student:
        for late in first_student:
            if late ==0:
                late = 1
            if late == 1:
                late= 0.9
            if late == 2:
                late= 0.75
            if late ==3:
                late =0.5
            else:
                late = 0
            average_1.append((grade + late)/len(first_student))
    for grade in second_student:
        for late in second_student:
            if late ==0:
                late = 1
            if late == 1:
                late= 0.9
            if late == 2:
                late= 0.75
            if late ==3:
                late =0.5
            else:
                late = 0
            average_2.append((grade + late)/len(second_student))
    for grade in third_student:
        for late in third_student:
            if late ==0:
                late = 1
            if late == 1:
                late= 0.9
            if late == 2:
                late= 0.75
            if late ==3:
                late =0.5
            else:
                late = 0
            average_3.append((grade + late)/len(third_student))
    return [sum(average_1), sum(average_2), sum(average_3)]



            
