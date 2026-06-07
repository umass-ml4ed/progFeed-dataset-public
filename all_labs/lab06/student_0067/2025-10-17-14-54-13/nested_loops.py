# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED




def get_names(first, last):
    full_names = []
    for c in first:
        for j in last:
            full_names.append(c + " " + j)
    return full_names



def average_scores(grades):
    final_scores = []


    for grade in grades:
        individual_scores = 0
        for j in grade:
            if j[1] == 0:
                individual_scores += j[0]
            elif j[1] == 1:
                individual_scores += j[0] * 0.9
            elif j[1] == 2:
                individual_scores += j[0] * 0.75
            elif j[1] == 3:
                individual_scores += j[0] * 0.5
            elif j[1] == 4:
                individual_scores += 0
        final_scores.append(individual_scores / len(grade))
    return final_scores
    
        
        

        
    


