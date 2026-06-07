# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def combine_lists(a,b):
   #Inserts first element of b at beginning of a
   a.insert(0, b[0])
   # Inserts last element of b at end of a
   a.append(b[-1])
    
   # Deletes middle element of a 
   middle_index = len(a) // 2  
   a.pop(middle_index)

   return a
#print(combine_lists([1, 2, 3],[4, 5, 6, 7]))
#print(combine_lists([1, 2, 3, 4, 5],[4, 5, 6, 7]))