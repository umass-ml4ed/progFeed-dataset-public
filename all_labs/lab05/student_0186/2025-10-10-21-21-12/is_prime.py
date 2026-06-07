def is_prime(n):
    flag=True
    div_n=2
    while div_n<(div_n**0.5)+1:
       if n % div_n==0:
           return False
       else:
           return True
    div_n=div_n+1



