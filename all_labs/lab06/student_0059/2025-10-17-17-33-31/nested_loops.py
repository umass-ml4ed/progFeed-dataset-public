# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
def get_names(first_names, last_names):
    full_names = []
    for f in first_names:
        for l in last_names:
            x = (f + " " + l)
            full_names.append(x)
    return full_names
print(get_names(first_names, last_names))


scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
def average_scores(lis):
    avg_lis = []
    
    for person in lis:
        total = 0
        for grade in person:
            num = grade[0] 
            if grade[1] == 0:
                total += num
            elif grade[1] == 1:
                total += num * 0.9
            elif grade[1] == 2:
                total += num * 0.75
            elif grade[1] == 3:
                total += num * 0.50
            else:
                total += num * 0
        average = total/len(person)
        avg_lis.append(average)
    return avg_lis

print(average_scores(scores))

        
            
