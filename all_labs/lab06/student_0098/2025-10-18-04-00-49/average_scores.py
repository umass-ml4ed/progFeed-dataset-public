# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def average_scores(all_assignments):
    averages = []
    
    for student_assignments in all_assignments:
        total_adjusted_score = 0
        assignment_count = 0
        
        for assignment in student_assignments:
            grade = assignment[0]
            lateness = assignment[1]
            
            adjusted_score = grade - lateness
            
            if adjusted_score < 0:
                adjusted_score = 0
                
            total_adjusted_score += adjusted_score
            assignment_count += 1
        
        if assignment_count > 0:
            average = total_adjusted_score / assignment_count
        else:
            average = 0
            
        averages.append(average)
        
    return averages

        
