# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

'''Your first exercise is to write a function called get_names which takes two lists of strings:
 one representing a list of first names (given names), the other a list of last names (surnames), 
 and the function returns a new list that contains all combinations of first names and last names. For example, if

first_names = ['Ari', 'Taylor']
	last_names = ['Levine', 'Lopez', 'Khan', 'Wang']

Your function should return a new list that contains 8 full names:
['Ari Levine', 'Ari Lopez', 'Ari Khan', 'Ari Wang', 'Taylor Levine',
	 'Taylor Lopez', 'Taylor Khan', 'Taylor Wang']

Specifically, write the function in the same file as before, and it should:
Take two lists of strings as parameters, one first_names, the other last_names
Use full_names=[] to create an empty list named full_names. 
Use nested for loops to iterate over the lists of first names and last names. 
For each combination of first name and last name, generate the full name, 
and append that to the full_names list. Each full name must have a space character between the first name and the last name.
After the loop, return the full_names list.
Do NOT ask the user for any input. Do NOT print anything in your function.
'''

def get_names(first_names, last_names):
   full_names = []
   for f_name in first_names:
      for l_name in last_names:
         full_names.append({first_names} + ' ' + {last_names})
         return full_names
      
'''In this exercise, you will write a function called average_scores that calculates 
the average grade for each student after applying a lateness penalty. 
The input is a list of lists, where each inner list represents a student's assignments. 
Each assignment is represented as a tuple of (grade, lateness). 
Grades are between 0 and 100 inclusive. For example: 
[[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
As you can see, it’s a list of lists of tuples: the size of the top-level list is the number of students 
(so there are 3 students in the example above) where each sub-list contains assignments for a student. Each assignment is represented as a 2-element tuple in a format of (raw grade, lateness). Specifically, your function should:
Take the input described above as the parameter. 
Apply the lateness penalty as follows:
Lateness = 0 → 100% credit (no penalty)
Lateness = 1 → 90% credit
Lateness = 2 → 75% credit
Lateness = 3 → 50% credit
Lateness ≥ 4 → 0% credit
Return a list where each element is the average grade of each student after applying penalties.
Do NOT ask the user for any input. Do NOT print anything in your function. '''


def average_scores(lis):
    avg_lis = []
   
    for student in lis:
      total = 0
      for grade, lateness in student:
            if lateness == 0:
                f_grade += grade
            elif lateness == 1:
                f_grade += grade * .9
            elif lateness == 2:
                f_grade += grade * .75
            elif lateness == 3:
                f_grade += grade * .50
            elif lateness >= 4:
                f_grade += grade * 0
                return f_grade  
            avg_lis.append(f_grade / len(student))
    return avg_lis


    



    



