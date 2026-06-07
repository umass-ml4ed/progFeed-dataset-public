# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(given_names:list, surnames:list):
    full_names = []
    for first_name in given_names:
        for last_name in surnames:
            full_names.append(str(first_name) + ' ' + str(last_name))
    return full_names

def average_scores(given_scores:list):
    after_penalty = []
    for student_score in given_scores:
        avg_score = 0
        for subjects in student_score:
            lateness = subjects[1]
            lateness_score = 1
            if lateness == 0:
                lateness_score = 1
            elif lateness == 1:
                lateness_score = 0.9 
            elif lateness == 2:
                lateness_score = 0.75
            elif lateness == 3:
                lateness_score = 0.5
            elif lateness >= 4:
                lateness_score = 0
            ef_mark = lateness_score*subjects[0]
            avg_score += ef_mark
        avg_score = avg_score/len(student_score)
        after_penalty.append(avg_score)   

    return after_penalty