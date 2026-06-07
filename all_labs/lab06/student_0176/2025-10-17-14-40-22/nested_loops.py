# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names (firstlst, lastlst): 
    full_names =[]
    for n in firstlst: 
        for i in lastlst: 
            name = firstlst[n] + " " + lastlst[i]
            full_names.append(name)

    return full_names

def average_scores(lst): 
    for i in range(len(lst)): 
        average = 0
        op =[]
        for n in range(len(lst[i])):
            lateness = int(lst[i][n][1])
            credit = int(lst[i][n][0])
            if lateness == 0:
                new = 1.00 * credit
            elif lateness == 1:
                new = 0.90 * credit
            elif lateness == 2:
                new = 0.75 * credit
            elif lateness == 3:
                new = 0.5 * credit
            else:
                new = 0 * credit
            average += new
        op.append(average)
    return op



        

            
            

                



        
