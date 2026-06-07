def print_stars_to_file(n):
    n = int(n)
    f1 = open(f'stars_{n}.txt','w')
    for a in range(1,n+1):
        for b in range(0,(n-a)):
            f1.write(" ")
        for c in range(0,((2*a) -1)):
            f1.write("*")
        f1.write("\n")

# print_stars_to_file(3)


def calc_avg_from_file():
    f1 = open('grades.txt','r')
    text = f1.read()
    lst = text.split('\n')
    sum = 0
    for a in lst:
        sum += float(a)
    return (sum/len(lst)) 

# print(calc_avg_from_file())