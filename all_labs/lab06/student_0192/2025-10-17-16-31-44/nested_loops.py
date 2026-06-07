# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(str1, str2):
    full_names = []
    for i in range(len(str1)):
        for k in range(len(str2)):
            full_names.append(f'{str1[i]} {str2[k]}')
    return full_names

print(get_names(['Ari', 'Taylor'], ['Levine', 'Lopez', 'Khan', 'Wang']))






def average_scores(x):
    final = []
    for lst in x:
        finscore = 0
        for grade, late in lst:
            if late == 0:
                penalty = 1
            elif late == 1:
                penalty = 0.9
            elif late == 2:
                penalty = 0.75
            elif late == 3:
                penalty = 0.5
            else:
                penalty = 0
            finscore += grade * penalty
        avg = finscore/len(lst)
        final.append(avg)
    return final


scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(scores))

           
            
                




