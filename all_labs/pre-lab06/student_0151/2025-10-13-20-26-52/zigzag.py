def longest_zigzag_from_start(lst):
  n = len(lst)
  if n < 3:
    return n
  count = 0
  for i in range(1, n):
    left = lst[i-1]
    mid = lst[i]
    right = lst[i+1]
    if (left < right and mid < left and mid < right) or (left > right and mid > left and mid > right):
      count += 1
    else:
      return count




def zigzag_lengths_from_all_starts(lst):
  res = []
  for i in range(len(lst)):
    part = lst[i:]
    leng = longest_zigzag_from_start(part)
    res.append(leng)
    
  return res

