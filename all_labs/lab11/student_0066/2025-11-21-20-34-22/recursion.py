# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def max_recursive(nums:list):
    
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    
    sub_interval = max_recursive(nums[1:])
    
    if nums[0] > sub_interval:
        return nums[0]
    else:
        return sub_interval
    
z = [1, 2, 3, 100]
w = [4, 5, 6, 0]





def sum_lists_recursive(nums1:list, nums2:list):
    
    if len(nums1) == 0:
        return 0
    
    
    return nums1[0] + nums2[0] + sum_lists_recursive(nums1[1:], nums2[1:])
    
    
    
    
    
# print(sum_lists_recursive(w, z))


def funky(n:int):
    
    if n == 0:
        return 0 
    elif (n == 1):
        return 1
    elif n % 2 == 0:
        return 2 * funky(n // 2)
    else:
        return 1 + 2 * funky(n+1)
    

z = ['A', 'B', 'C', 'D']

def permutations(things:list):
    
    if len(things) <= 1:
        return [things]
    
    ans = []
    
    for i in range(len(things)):
        front = things[i]
        
        remaining = things[:i] + things[i+1:]
        
        subthings = permutations(remaining)
        
        for perm in subthings:
            ans.append([front]+ perm)
            
    return ans
    


print(funky(-50))          
    