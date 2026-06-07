# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

first_name=['Ari', 'Taylor']
last_name=['Levine', 'Lopez', 'Khan', 'Wang']
def get_names(first_name,last_name):
 full_names=[]
 for a in first_name:
  for b in last_name:
   full_names.append(f'{a}{b}')
 return full_names

score=[[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
def average_scores(scores):
 result=[]
 for student in scores:
  total=0
  for grade, lateness in student:
   if lateness==0:
    penalty=1
   elif lateness==1:
    penalty==0.9
   elif lateness==2:
    penalty==0.75
   elif lateness==3:
    penalty==0.5
   else:
    penalty==0
   total+=grade*penalty
 avg=total/len(student)
 result.append(avg)
 return result