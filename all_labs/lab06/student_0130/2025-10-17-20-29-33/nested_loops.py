#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def get_names(first_names, last_names):
    full_names= []
    for first in first_names:
        for last in last_names:
            full_name= first + " " + last
            full_names.append(full_name)
    return full_names


def average_scores (students):
    averages= []
    for student in students:
        total=0
        count=0 
        for grade, lateness in student:
            if lateness==0:
                adjusted= grade 
            elif lateness==1:
                adjusted= grade *0.9 
            elif lateness==2:
                adjusted= grade * 0.75 
            elif lateness==3: 
                adjusted= grade * 0.5 
            else: 
                adjusted= 0
            total+= adjusted
            count+= 1 
        average= total/count if count>0 else 0
        averages.append(average)
    return averages 