# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def print_stars_to_file(n):
    with open(f"stars_{n}.txt","w") as binglebongle:
        for i in range(n):
            dingledangle=(2*(i+1))-1
            binglebongle.write(" "*(n-1-i)+"*"*dingledangle)
            
