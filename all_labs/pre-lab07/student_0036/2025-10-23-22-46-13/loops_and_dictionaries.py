def pyramid(n):
    pyramid=""
    for i in reversed(range(n)):
        for j in reversed(range(1,i+2)):
            pyramid+=str(j)
        pyramid+="\n"
        #pyramid+=f"{list(reversed(range(1,i+2)))}"+"\n"
    return pyramid

print(pyramid(4))