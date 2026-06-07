# Author  : REDACTED
# Email : REDACTED
# Spire ID  : REDACTED

def get_names(first_names, last_names):
    full_names = []
    for f in first_names:
        for l in last_names:
            combo = f + ' ' + l
            full_names.append(combo)
    return full_names

print(get_names(['Jordie', 'Benny'], ['Hillary', 'Carson', 'Allukwae']))

def average_scores(raw_grade, lateness):
    scores = [[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]
    lateness = [0, 1, 2, 3, 4]
    lateness[0] = int('')
    lateness[1] = 0.9
    lateness [2] = 0.75
    lateness[3] = 0.5
    lateness[4] = 0
    for r in raw_grade:
        for l in lateness:
            scores = raw_grade*lateness
    return scores

print(average_scores([scores]))
    