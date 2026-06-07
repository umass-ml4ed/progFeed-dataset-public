






    
    
def count_words(words):
    freq = {}
    
    for l in words:
        if l not in freq:
            freq[l] = 1
        else:
            freq[l] += 1
    
    return freq
                
        
