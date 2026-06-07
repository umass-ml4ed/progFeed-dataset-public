# Authors   : REDACTED
# Emails    : REDACTED
# Spire ID REDACTED

n=int(input("Enter a positive number: "))
sum=0
i=1
if n>0:
    while i<=n:
        sum+=(i**(-2))
        i+=1
    print("sum = ", sum)
else:
    print('Enter a POSITIVE number!')
pi=(6*sum)**0.5
print('approximate value of pi is:', pi)