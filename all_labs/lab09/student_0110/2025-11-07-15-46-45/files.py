# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def print_stars_to_file(n):
    stars = open(f"starst_{n}.txt", 'w')
    count = 1
    for i in range(n):
        stars.write(" "*(n - (i + 1))+"*"*(count)+"\n")
        count += 2
    stars.close()

def calc_avg_from_file():
    grades = open("grades.txt")
    text = grades.read()
    grades.close()
    new_text = text.split()
    total = 0
    for num in new_text:
        total = total + float(num)
    return total/len(new_text)

