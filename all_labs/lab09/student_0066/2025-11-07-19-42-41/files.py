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
     
     
def calc_avg_from_file():
    with open("grades.txt") as f:
        data = f.read().split("\n")  
    
    things = []
    
    for num in data:
        z = float(num)
        things.append(z)
        
        
    ans = 0
    
    for num in things:
        ans += num / len(data)
        
    return ans
        
        
print(calc_avg_from_file())