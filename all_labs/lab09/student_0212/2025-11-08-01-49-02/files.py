# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    file = open("./stars_" + str(n) + ".txt", "w")
    num = n
    row = 1
    while row <= n:
        file.write(" " * (n - row))
        file.write("*" * ((2 * row) - 1) + "\n")
        row += 1

def calc_avg_from_file():
    file = open("./grades.txt", "r")
    text = file.readlines()

    list = []
    for index in range(0, len(text) - 1):
        list.append(text[index][0:-1:1])
    list.append(text[-1])
    
    float_list = []
    for index_2 in range(0, len(list)):
        float_list.append(float(list[index_2]))


    total = 0
    for num in float_list:
        total += num
    return total / len(float_list)
