# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file(n):
    with open(f'./stars_{n}.txt', 'w') as file:
        for i in range(1, n+1):
            file.write(((n-i)*' ')+((2*i)-1)*'*'+'\n')
#print_stars_to_file(3)

def calc_avg_from_file():
    with open('./grades.txt', 'r') as file:
        text=file.read()
        grades=text.split('\\n')
        total=0
        count=0
        for i in grades:
            x=float(i)
            total+=x
            count+=1
        a=total/count
    return(a)
print(calc_avg_from_file())