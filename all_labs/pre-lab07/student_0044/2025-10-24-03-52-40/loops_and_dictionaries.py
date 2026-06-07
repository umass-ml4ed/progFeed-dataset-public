# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

#print('abc\ndef')
def pyramid(n):
    x=''
    for a in range(n, 0, -1) :
        for b in range(a, 0, -1):
            if b==1:
                x+=str(b),
            else:
                x+=str(b)+' '
    return(x)
print(pyramid(4))

#def merge_dicts(d1, d2):
#    d1.copy()
#    while d1 in d2:
#        
    