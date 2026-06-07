# # Author: REDACTED_NAME
# # Email: REDACTED_EMAIL
# # Spire ID: REDACTED_SPIRE_ID

def get_names(first_names, last_names):
    full_names = []
    for first in first_names:
        for last in last_names: 
            full_names.append(f"{first} {last}")
    return full_names

def average_scores(all_scores):
    result = []
    for student in all_scores:
        total = 0
        count = 0
        for grade, lateness in student:
            if lateness == 0:
                penalty = 1.0
            elif lateness == 1:
                penalty = 0.9
            elif lateness == 2:
                penalty = 0.75
            elif lateness == 3:
                penalty = 0.5
            else:
                penalty = 0.0
            total += grade * penalty
            count += 1
        if count > 0:
            average = total / count
        else:
            average = 0.0
        result.append(average)
    return result

# Example usage (can be removed before submitting):
if __name__ == "__main__":
    first_names = ['Ari', 'Taylor']
    last_names = ['Levine', 'Lopez', 'Khan', 'Wang']
    print(get_names(first_names, last_names))
    
    scores = [
        [(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)],
        [(100, 10), (90, 0), (80, 0), (90, 0)],
        [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]
    ]
    print(average_scores(scores))