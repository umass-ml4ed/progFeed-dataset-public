# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(g_names, surnames):
    outer = 0
    inner = 0
    lst = []
    while(outer < len(g_names)):
        inner = 0
        while(inner < len(surnames)):
            lst.append(str(g_names[outer]) + " " + str(surnames[inner]))
            inner += 1
        outer += 1
    return lst

def average_scores(grades):
    student_i = 0
    test_i = 0
    percentage = 0
    sum_tests = 0
    lst = []
    while(student_i < len(grades)):
        test_i = 0
        sum_tests = 0
        while(test_i < len(grades[student_i])):
            if grades[student_i][test_i][1] == 0:
                percentage = 100
            elif grades[student_i][test_i][1] == 1:
                percentage = 90
            elif grades[student_i][test_i][1] == 2:
                percentage = 75
            elif grades[student_i][test_i][1] == 3:
                percentage = 50
            else:
                percentage = 0
            sum_tests += (grades[student_i][test_i][0]) * (percentage) / 100
            test_i += 1
        lst.append(sum_tests / len(grades[student_i]))
        student_i += 1
    return lst