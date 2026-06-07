# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def filter_positive(numbers):
    pos_list = []
    for num in numbers:
        if num > 0:
            pos_list.append(num)
        return pos_list
    
if __name__ == "__main__":
    print(filter_positive([1, -3, 5, 0, -2, 7])) 
    print(filter_positive([-5, -1, -10]))          
    print(filter_positive([10, 20, -30, 40]))      