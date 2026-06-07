def get_names(arg1, arg2):
    # Placeholder: Replace arg1, arg2 with required logic
    # Return a list of names based on assignment instructions
    return []

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
