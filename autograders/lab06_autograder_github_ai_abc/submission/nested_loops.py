def get_names(first_names, last_names):
    names = []
    for first in first_names:
        for last in last_names:
            names.append(f"{first} {last}")
    return names

def average_scores(students):
    averages = []
    for student in students:
        total = 0
        for score in student:
            grade, late = score
            if late == 1:
                grade = grade * 0.9
            elif late == 2:
                grade = grade * 0.75
            elif late == 3:
                grade = grade * 0.5
            elif late >= 4:
                grade = 0
            total += grade
        avg = total / len(student)
        averages.append(avg)
    return averages

if __name__ == "__main__":
    print(average_scores ([[ (100, 4), (50, 4), (75, 0) ]]))
    print(average_scores([[ (90, 0), (80, 1), (70, 2), (60, 3), (50, 4), (100, 1) ]]))