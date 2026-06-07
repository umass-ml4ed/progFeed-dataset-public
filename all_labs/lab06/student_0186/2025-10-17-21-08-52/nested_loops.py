def get_names(fname_list,lname_list):
    full_names=[]
    c=0
    for i in fname_list:
        for g in lname_list:
            full_names.append(i+" "+g)
    return full_names
def average_scores(score_list):
    avg=0
    sum=0
    for i in score_list:
        for g in score_list:
            sum=sum+score_list[i][g][0]
            if score_list[i][g][1]==1:
                sum=sum*0.9
            if score_list[i][g][1]==2:
                sum=sum*0.75
            if score_list[i][g][1]==3:
                sum=sum*0.5
            if score_list[i][g][1]>=4:
                sum=0
            c=c+1
            avg=sum/c
    return avg

        
            

             


