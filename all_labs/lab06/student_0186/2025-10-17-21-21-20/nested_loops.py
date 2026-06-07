def get_names(fname_list,lname_list):
    full_names=[]
    c=0
    for i in fname_list:
        for g in lname_list:
            full_names.append(i+" "+g)
    return full_names
def average_scores(score_list):
    averages = []            

    for student in score_list:
        total = 0            
        count = 0             


        for grade, lateness in student:

            if lateness == 0:
                penalty = 1
            elif lateness == 1:
                penalty = 0.9
            elif lateness == 2:
                penalty = 0.75
            elif lateness == 3:
                penalty = 0.5
            else:
                penalty = 0


            total += grade * penalty
            count += 1

  
        avg = total / count
        averages.append(avg)

    return averages

        
            

             


