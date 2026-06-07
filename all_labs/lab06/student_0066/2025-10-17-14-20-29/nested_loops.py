first_names = ['Ari', 'Taylor']
last_names = ['Levine', 'Lopez', 'Khan', 'Wang']



def get_names(A:list, B:list):
    full_names=[]
    
    for k in range(len(first_names)):
        for i in range(len(last_names)):
            full = first_names[k] + " " + last_names[i]
            full_names.append(full)
            
            
    return full_names

