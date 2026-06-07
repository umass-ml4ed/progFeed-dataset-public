# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def print_stars_to_file (n): 
    name = f"stars_{n}.txt"
    fil = open(name, "w")
    for i in range(n): 
        print(((n-i+1)*" " + (i+1+i*1)*"*"), file=fil)

def calc_avg_from_file(): 
    fil = open("grades.txt", "r")
    text=fil.read()
    text = text.split("\n")
    sum = 0
    for num in text: 
        n = float(num)
        sum += n
    average = sum / (len(text))


