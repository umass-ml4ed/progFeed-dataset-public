# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED
b = [0,1,2,3]
b[1]
def is_zigzag(a):
    if len(a) == 1:
        return (True)
    for n in range(0,len(a)):
        if a[n] == a[-1]:
            a = a
        elif (a[n-1] < a[n] > a[n+1]) or (a[n-1] > a[n] < a[n+1]):
            a = a 
        else:
            return (False)
    return (True)


