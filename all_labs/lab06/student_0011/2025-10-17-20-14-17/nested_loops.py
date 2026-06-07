#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def get_names(first, last):
    full_names = []
    for i in first:
        for x in last:
            full_names.append(i + " " + x)
    return full_names
        
def average_scores(list):
    output =[]
    for student in list:
        x = 0
        for i in student:
            if i[1]==0:
                x=x+i[0]
            elif i[1]==1:
                x = x+i[0]*.9
            elif i[1]==2:
                x=x+i[0]*.75
            elif i[1]==3:
                x=x+i[0]*.5
            else:
                x=x
        output.append(x/len(student))
    return output

scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], 
          [(100, 10), (90, 0), (80, 0), (90, 0)], 
          [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
print(average_scores(scores))