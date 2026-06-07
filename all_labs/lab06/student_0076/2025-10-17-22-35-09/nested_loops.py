# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
 full_names = []
 for first in first_names:
  for last in last_names:
   full_names.append(f"{first} {last}")
 return full_names


def average_scores(scores):
 result = []
 for student in scores:
  total = 0
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
  avg = total / len(student)
  result.append(avg)
 return result