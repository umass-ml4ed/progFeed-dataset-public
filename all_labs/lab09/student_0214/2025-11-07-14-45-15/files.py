# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def print_stars_to_file(n):
    f = open(f"stars_{n}.txt", "w")
    for num in range(1,n + 1):
        print((" " * (n-num)) + ("*" * (2 * num - 1)), file = f)
    f.close()
print_stars_to_file(6)
def calc_average_from_file():
    f = open("grades.txt", "r")
    text = f.read()
    lst = text.split("\n")
    n = 0
    total = 0
    for x in lst:
        total += float(x)
        n +=1
    f.close()
    return total / n
calc_average_from_file()




