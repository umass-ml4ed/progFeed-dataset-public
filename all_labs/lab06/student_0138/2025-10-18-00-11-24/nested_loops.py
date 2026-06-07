# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def is_prime(n):
    if n < 2:
        return False
    div = 2
    while div <= int(n ** 0.5):
        if n % div == 0:
            return False
        div += 1
    return True

def get_names(first_names,last_names):
    full_names = []
    for f in first_names:
        for l in last_names:
            full_names.append(f"{f} {l}")
    return full_names

def average_scores(scores):
    for s in scores:
        student1 = []
        student2 = []
        student3 = []
        for s_b in scores[0]:
            for s_b_s in scores[0][0]:
                