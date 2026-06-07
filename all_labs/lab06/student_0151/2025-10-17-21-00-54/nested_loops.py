def get_names(f,l):
  res = []
  for i in f:
    for j in l:
      res.append(f[i] + " " + l[j])
  return res

def average_scores(lsd):
  n = len(lsd)
  res = []
  sum = 0
  count = 0
  for i in lsd:
    for j in lsd:
      
      if lsd[i][j][1] == 0:
        sum += lsd[i][j][0]
      elif lsd[i][j][1] == 1:
        sum += lsd[i][j][0] * 0.9
      elif lsd[i][j][1] == 2:
        sum += lsd[i][j][0] * 0.75
      elif lsd[i][j][1] == 3:
        sum += lsd[i][j][0] * 0.5
      else:
        sum += 0
      count += 1
    res.append(sum/count)
  return res



  
      