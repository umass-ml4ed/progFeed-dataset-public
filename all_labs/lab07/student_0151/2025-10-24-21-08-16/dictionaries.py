def count_words(lst):
  dict = {}
  for i in lst:
    if i in dict:
      dict[i] += 1
    else:
      dict[i] = 1
  return dict


def average_prices(lst):
  dict = {}
  count = {}
  for char,val in lst:
    if char in dict:
      dict[char] += val
      count[char] += 1
    else:
      dict[char] = val
      count[char] = 1
    if char in count:
      dict[char] = dict[char]/count[char]
  return dict


print(average_prices((('gouda cheese 1 lbs', 3.49), ('organic oyster mushroom 1 lbs', 6.89), ('toilet paper 1 roll', 3.99), ('apple juice 1 gallon', 7.99), ('gouda cheese 1 lbs', 4.29), ('toilet paper 1 roll', 4.19), ('talenti gelato vanilla', 5.59))))
  

def count_bigrams(words):
  bigram_counts = {}
  
  # Only proceed if there are at least 2 words
  for i in range(len(words) - 1):
      bigram = (words[i], words[i + 1])
      bigram_counts[bigram] = bigram_counts.get(bigram, 0) + 1
  
  return bigram_counts