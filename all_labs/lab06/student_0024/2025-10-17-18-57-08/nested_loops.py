def get_names(first_names, last_names):
    full_names = []
    for first in first_names:
        for last in last_names:
            full_names.append(f"{first} {last}")
    return full_names
print(get_names(("Ari", "Taylor"), ("Levine", "Lopez")))


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
