# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def pyramid(n):
    i=n
    result =""
    for i in range(n,0,-1):
        line=[str(i) for i in range(n,0,-1)]
        result= result + " ".join(line) + "\n"
        n = n- 1
    print(result)

pyramid(4)






