# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def pyramid(n):
    pyramid=""
    for i in reversed(range(n)):
        for j in reversed(range(1,i+2)):
            pyramid+=str(j)+" "
        pyramid.strip()
        pyramid+="\n"
    return pyramid

print(pyramid(4))
print(pyramid(6))
print(pyramid(5))
print(pyramid(3))