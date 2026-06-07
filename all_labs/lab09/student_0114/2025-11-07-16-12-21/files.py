# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

#file = open('./my_file.txt', 'w')
#file.write('Hello, world!')
#file.close()
#file = open('./my_file.txt', 'r')
#contents = file.read()
#print(contents)

def print_stars_to_file(n):
    file = open(f"./stars_{n}.txt", mode = "w")
    count = 0
    str = ''
    while count < n:
        str += (" "*(n-count - 1) + "*" * (1 + 2*count) + "\n")
        count += 1
    file.write(str)
    file.close()
    file = open(f"./stars_{n}.txt", "r")
    contents = file.read()
    print(contents)

#print_stars_to_file(1)
#print_stars_to_file(2)
#print_stars_to_file(3)
#print_stars_to_file(6)

def calc_avg_from_file():
    f = open("./grades.txt", "r")
    text = f.read()
    text = text.split("\n")
    avg = 0
    for num in text:
        avg += float(num)
    avg /= len(text)
    f.close()
    return avg

#print(calc_avg_from_file())