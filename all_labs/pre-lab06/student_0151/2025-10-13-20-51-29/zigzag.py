def longest_zigzag_from_start(lst):
  n = len(lst)
  if n < 3:
    return n
  count = 2
  for i in range(1, n-1):
    left = lst[i-1]
    mid = lst[i]
    right = lst[i+1]
    diff1 = mid - left
    diff2 = mid - right
    if (diff1 > 0 and diff2 > 0) or (diff1 < 0 and diff2 < 0):
      count += 1
    else:
      return count
    

print(longest_zigzag_from_start([1,2,3,4,5]))



def zigzag_lengths_from_all_starts(lst):
  res = []
  for i in range(len(lst)):
    part = lst[i:]
    leng = longest_zigzag_from_start(part)
    res.append(leng)
    
  return res

