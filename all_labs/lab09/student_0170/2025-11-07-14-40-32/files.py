# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    stars = 1
    filename = ("stars_" + str(n) + ".txt")
    with open(filename,"w") as file:
        while n > 0:
            res = ""
            for i in range(n-1):
                res += " "
            for i in range(stars):
                res += "*"
            res += "\n"
            n -= 1
            stars += 2
            file.write(res)
    file.close

def calc_avg_from_file():
    with open("grades.txt","r") as file:
        text = file.read()
        numlist = text.split('\n')
        print(numlist)
        sum = 0
        for i in numlist:
            sum += float(i)
        if len(numlist) > 0:
            return sum/len(numlist)
        else:
            return 0