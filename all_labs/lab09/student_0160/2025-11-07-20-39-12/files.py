def print_stars_to_file(n):
    file =  open(f'stars_{n}.txt', 'w')
    for x in range(1,n+1):
        a = int(n-x)
        int(n)
        file.write(a*' ')
        file.write((2*x-1)*'*' + '\n')

def calc_avg_from_file():
    file =  open('grades.txt', 'r')
    text=file.read()
    lst = text.split('\n')
    avg = 0
    for element in lst:
        avg += float(element)
    total_avg = avg/len(lst)
    return total_avg