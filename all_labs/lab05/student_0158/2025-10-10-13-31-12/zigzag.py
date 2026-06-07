# Authors   : REDACTED
# Emails    : REDACTED
# Spire ID REDACTED

def is_zigzag(list):
    z=0
    if len(list)<3:
        return True
    else:
        for i in range(len(list)-2):
            if (list[i+1]>list[i] and list[i+1]>list[i+2]) or (list[i+1]<list[i] and list[i+1]<list[i+2]):
                z+=1
        print(z)
        if z==len(list)-2:
            return True
        else:
            return False
        


