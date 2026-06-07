






    
    
def count_words(words):
    freq = {}
    
    for l in words:
        if l not in freq:
            freq[l] = 1
        else:
            freq[l] += 1
    
    return freq
                
        

def average_prices(A):
    
    count = {}
    total = {}
    
    for name, price in A:
        if name not in total:
            total[name] = price
            count[name] = 1
        else:
            total[name] += price
            count[name] += 1
            
    average = {}
    
    for thing in total:
        average[thing] = total[thing] / count[thing]
        
        
    return average
            
    



