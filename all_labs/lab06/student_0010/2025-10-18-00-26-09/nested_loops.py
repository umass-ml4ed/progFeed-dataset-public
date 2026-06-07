# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def get_names(list1, list2):
        full_names = []
        for first in list1:
                for last in list2:
                        full_name = first + ' ' + last
                        full_names.append(full_name)
        return full_names



def average_scores(list1):
        final = []
        for assignments in list1:
                score = 0.0
                num_of_assignments = len(assignments)
                for assignment in assignments:
                        grade = assignment[0]
                        lateness = assignment[1]
                        penalized = 0.0
                        if lateness == 0:
                                penalized = grade * 1.0 
                        elif lateness == 1:
                                penalized = grade * 0.9  
                        elif lateness == 2:
                                penalized = grade * 0.75 
                        elif lateness == 3:
                                penalized = grade * 0.5  
                        else:  
                                penalized = grade * 0.0  
                        score += penalized
                if num_of_assignments > 0:
                        average = score / num_of_assignments
                else:
                        average = 0.0

                final.append(average)
        return final

