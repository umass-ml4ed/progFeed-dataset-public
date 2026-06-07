# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED





with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")
  
  
  
def print_stars_to_file(n:int):
    
    name = "stars_" + str(n) + ".txt"
    
    with open(name, "a") as f:
        
        for k in range(n):
            the_line = " " * (n - k - 1) + "*" * (2 * k + 1)
            
            f.write(the_line + "\n")
     
     
print_stars_to_file(31)