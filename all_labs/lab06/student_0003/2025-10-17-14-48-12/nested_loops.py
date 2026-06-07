# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(lst1, lst2):
    full_names=[]
    for first_names in lst1:
        for last_names in lst2:
            full_names.append(first_names+" "+last_names)
    print(full_names)
    return full_names

def average_scores(scores):
    new_score=0
    f_lst=[]
    for student in scores:
        total=0
        for assignment in student:
            print(assignment)
            if assignment[1]==0:
                new_score=assignment[0]
            elif assignment[1]==1:
                new_score=0.9*assignment[0]
            elif assignment[1]==2:
                new_score=0.75*assignment[0]
            elif assignment[1]==3:
                new_score=0.5*assignment[0]
            elif assignment[1]>=4:
                new_score=0
            print(new_score)
            total += new_score
            
        avg= total/len(student)
        f_lst.append(avg)
    
    return f_lst




            

