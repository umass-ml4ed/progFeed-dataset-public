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
  count = count_words(lst)
  for char,val in lst:
    if char in dict:
      dict[char] += val
    else:
      dict[char] = val
    if char in count:
      dict[char] = dict[char]/count[char]
  return dict


    
  

def count_bigrams(words):
  bigram_counts = {}
  
  # Only proceed if there are at least 2 words
  for i in range(len(words) - 1):
      bigram = (words[i], words[i + 1])
      bigram_counts[bigram] = bigram_counts.get(bigram, 0) + 1
  
  return bigram_counts