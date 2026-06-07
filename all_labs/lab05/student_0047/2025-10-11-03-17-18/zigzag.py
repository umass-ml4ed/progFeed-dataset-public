# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(list):
    count=0
    if (len(list)<3):
        return True
    else:
        for num in range(1,len(list)-1):
            #print ("NUM:",num)
            if ((list[num]>list[count] and list[num]>list[count+2])  or (list[num]<list[count] and list[num]<list[count+2])):
               # print("before:", list[count])
                #print ("after:",list[count+2])
                count+=1
               # print("count",count)
            else:
                return False
    
    return True





