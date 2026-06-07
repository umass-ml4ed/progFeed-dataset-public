def is_prime(n):
    if n < 2:
        return False
    
    div_n = 2
    while div_n <= n**0.5:
        if n % div_n == 0:
            return False
        div_n = div_n + 1
        
    return True