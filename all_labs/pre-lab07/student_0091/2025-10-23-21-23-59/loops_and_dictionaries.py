# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
print('abc\ndef')
words=["cat", "and", "mouse"]
print("\n".join(words))


def pyramid(n):
    row=n
    result =""
    for row in range(n,0,-1):
        lines=[str(numb) for numb in range(row,0,-1)]
        result= " ".join(lines)
        print(result)
        row=row-1


pyramid(4)
    #line1=[n for n in range(n,0,-1)]
    #line2=[n for n in range(n-1,0,-1)]
    #line3=[n for n in range(n-2,0,-1)]
    #print(line1)
    #print(line2)
    #print(line3)








