# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

from typing import List, Tuple

def get_names(first_names: List[str], last_names: List[str]) -> List[str]:
    full_names: List[str] = []
    for first in first_names:
        for last in last_names:
            full_names.append(f"{first} {last}")
    return full_names

def average_scores(all_students: List[List[Tuple[float, int]]]) -> List[float]:
    averages: List[float] = []
    for student in all_students:
        if not student:
            averages.append(0.0)
            continue
        total = 0.0
        count = 0
        for grade, lateness in student:
            if lateness == 0:
                mult = 1.0
            elif lateness == 1:
                mult = 0.9
            elif lateness == 2:
                mult = 0.75
            elif lateness == 3:
                mult = 0.5
            else:
                mult = 0.0
            total += grade * mult
            count += 1
        averages.append(total / count if count > 0 else 0.0)
    return averages
