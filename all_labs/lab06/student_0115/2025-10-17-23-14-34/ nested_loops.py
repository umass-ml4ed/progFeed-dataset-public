# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def  get_names(first_names, last_names):
   full_names=[]
   for i in first_names:
         for j in last_names:
             full_name=i+" "+j
             full_names.append(full_name)
   return full_names

first_names=['Ari', 'Taylor']
last_names=['Levine', 'Lopez', 'Khan', 'Wang']
print(get_names(first_names, last_names))

def average_scores(scores):
    output=[]
    for i in scores:
        total=0
        number=0
        for k,j in i:
            if j==0:
                m=1.0
            elif j==1:
                m=0.9
            elif j==2:
                m=0.75
            elif j==3:
                m=0.5
            else:
                m=0.0
            total+=k*m
            number+=1
        output.append(total/number)
    return output
    
scores=[[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)],
        [(100, 10), (90, 0), (80, 0), (90, 0)],
        [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(scores))