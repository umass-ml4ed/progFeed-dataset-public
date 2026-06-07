# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def pyramid(n):
    for i in range(n, 0, -1):          
        for j in range(i, 0, -1):      
            print(j, end=' ')         
        print()     


def pyramid(n):
    result = ""
    for i in range(n, 0, -1):
       
        line = ""
        for j in range(i, 0, -1):
            line += str(j)
            if j > 1:  
                line += " "
        
       
        line += "\n"
        result += line
    
    return result