# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

def get_names(first_names,last_names):
    full_names = []
    for firstname in first_names :
        for lastname in last_names:
            name = firstname+" "+lastname
            full_names.append(name)
    return full_names


def avergae_scores(a):
    students = len(a)
    final_list = []
    for exams in a :
        avg_score = 0
        for score in exams:
            l_score = 1
            late = score[1]
            if (late == 0):
                l_score = 1
            elif (late == 1):
                l_score = 0.9
            elif (late == 2):
                l_score = 0.75
            elif (late == 3):
                l_score = 0.5
            elif (late == 4):
                l_score = 0
            grade = score[0] * l_score
            avg_score += grade 
        avg_score = avg_score/len(exams)
        final_list.append(avg_score) 
    
    return final_list

