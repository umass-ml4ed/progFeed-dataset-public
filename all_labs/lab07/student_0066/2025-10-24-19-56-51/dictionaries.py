






    
    
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
            
    
    
def count_bigrams(A):
    doubles = []
    
    for k in range(len(A) - 1):
        bi = (A[k], A[k + 1])
        
        doubles.append(bi)
        
    counter = {}
    
    for thing in doubles:
        if thing not in counter:
            counter[thing] = 1
        else:
            counter[thing] += 1
            
    return counter
        
        
    
    


