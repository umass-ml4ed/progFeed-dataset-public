def is_prime(n):
    i=2
    while i < (int(n**0.5)+1):
        if n%i == 0:
            return False
        i+=1
    return True

g=0
while g<30:
    print(f"{g}: {is_prime(g)}")
    g+=1