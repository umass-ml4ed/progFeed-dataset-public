def print_stars_to_file(n):
    try:
        with open (f"stars_{n}.txt", "x") as g:
            g.close()
    except:
        print("file already exists")
    
    with open(f"stars_{n}.txt", "a") as f:
        f.truncate(0)
        for i in range(n,0,-1):
            f.write(" "*i)
            f.write("*" * (2*n+1 - 2*i))
            f.write("\n")

def calc_avg_from_file():
    with open("grades.txt") as f:
        text = f.read()
        s = text.split("\n")

        avg = sum(list(map(float,s))) / len(s)

        return avg
    
print(calc_avg_from_file())