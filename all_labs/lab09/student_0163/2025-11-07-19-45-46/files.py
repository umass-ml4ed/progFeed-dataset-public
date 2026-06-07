# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open(f"stars_{n}.txt","w") as binglebongle:
        for i in range(n):
            dingledangle=(2*(i+1))-1
            binglebongle.write(" "*(n-1-i)+"*"*dingledangle+"\n")
            
def calc_avg_from_file():
    with open("grades.txt","r") as yickitydoo:
        yickitydah=yickitydoo.read()
        pingpong=yickitydah.split("\n")
        lippytappy=[]
        for i in pingpong:
            lippytappy.append(float(i))
        return sum(lippytappy)/len(lippytappy)
