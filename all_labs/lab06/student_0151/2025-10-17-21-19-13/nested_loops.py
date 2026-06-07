def get_names(f,l):
  res = []
  for i in range(len(f)):
    for j in range(len(l)):
      res.append(f[i] + " " + l[j])
  return res

def average_scores(lsd):
  n = len(lsd)
  res = []
  sum = 0
  late = 0
  
  for i in range(len(lsd)):
    count = 0
    for j in range(len(lsd[i])):
      
      if lsd[i][j][1] == 0:
        late = lsd[i][j][0] 
      elif lsd[i][j][1] == 1:
        late = lsd[i][j][0] 
        sum += late * 0.9
      elif lsd[i][j][1] == 2:
        late = lsd[i][j][0] 
        sum += late * 0.75
      elif lsd[i][j][1] == 3:
        late = lsd[i][j][0] 
        sum += late * 0.5
      else:
        sum += 0
      count += 1
    res.append(sum/count)
  return res



  
      