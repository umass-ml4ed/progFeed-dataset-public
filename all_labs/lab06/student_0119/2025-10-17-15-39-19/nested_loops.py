# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names,last_names):
    full_name=[]
    j=0
    for i in first_names:
        name=i
        for j in last_names:
            new_name=name + ' ' + j
            full_name.append(new_name)
    return full_name

def average_scores(scores):
    result=[]
    for student in scores:
        total=0
        count=0
        for i in student:
            grade=i[0]
            late=i[1]
            if late==0:
                n=1
            elif late==1:
                n=0.9
            elif late==2:
                n=0.75
            elif late==3:
                n=0.50
            else:
                n=0
            total+=grade*n
            count+=1
        avg=total/count
        result.append(avg)
    return result

