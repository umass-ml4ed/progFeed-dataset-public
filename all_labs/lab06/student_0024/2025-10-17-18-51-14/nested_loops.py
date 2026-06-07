def get_names(first_names, last_names):
    # Combinations of the one first name with all last names
    return [first_names[0] + " " + last_name for last_name in last_names]

def average_scores(scores):
    penalties = {0: 1.0, 1: 0.9, 2: 0.75, 3: 0.5}
    result = []
    for student in scores:
        total = 0
        for grade, late in student:
            penalty = penalties.get(late, 0)
            total += grade * penalty
        avg = total / len(student)
        result.append(avg)
    return result
