# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(L):
    option=''
    if len(L)<3:
        return True
    else:
        for i in range(1,len(L)-1):
            if L[i]>L[i-1] and L[i]>L[i+1]:
                option+='y'
            elif L[i]<L[i-1] and L[i]<L[i+1]:
                option+='y'
            else:
                option+='n'
        if 'n' in option:
            return False
        else:
            return True

print(is_zigzag([1, 3, 2, 4, 5]))   