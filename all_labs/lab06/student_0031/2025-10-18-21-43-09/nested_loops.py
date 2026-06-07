# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names,last_names):
    full = []
    for f in first_names:
        for l in last_names:
            full.append(f"{f}+' ' +{l}")
    return full

penalties = { 
    0 : float(1.0), 1 : float(0.9), 2 : float(0.75), 3 : float(0.5)
}


def average_scores(all_scores):
    averages = []
 
    for student in all_scores:
        tot = 0
        num_assignments = 0
        for grade,late in student:
            if late in penalties:
                real = grade * penalties[late]
            else:
                real = 0
            tot = tot + real
            num_assignments = num_assignments + 1
        avg = tot / num_assignments
        averages.append(avg)
    return averages
            
