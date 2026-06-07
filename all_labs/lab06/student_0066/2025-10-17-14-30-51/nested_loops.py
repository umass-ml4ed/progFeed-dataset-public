# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']



def get_names(A:list, B:list):
    full_names=[]
    
    for k in range(len(first_names)):
        for i in range(len(last_names)):
            full = first_names[k] + " " + last_names[i]
            full_names.append(full)
            
            
    return full_names

scores_list = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]


def average_scores(scores:list):
    ans = []
    
    for k in range(len(scores)):
        
        B = []
        
        for i in range(len(scores[k])):
            late = 1
            LATENESS = scores[k][i][1]
            if LATENESS == 0:
                late = 1
            elif LATENESS == 1:
                late = 0.9
            elif LATENESS == 2:
                late = 0.75
            elif LATENESS == 3:
                late = 0.5
            elif LATENESS >= 4:
                late = 0
                
            a = scores[k][i][0] * late
            
            B.append(a)
            
        avg = sum(B) / len(B)
        ans.append(avg)
        
    return ans

            
        
            
        