# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


#dict = {}
#def count_words(dict):
 #   for string in dict:
  #      if string in dict:
   #        dict(string) = string += 1
    #    
     #   else:
      #      dict(string) = 1
       #     return dict
        

    #return dict

#dictionary = {( 'a' , 'b')}
#def count_words(dictionary):
 #   for set in dictionary:
  #      if 'a' in dictionary:
   #         return dictionary
    #    else:
     #       dictionary.add(1)

#dict = {"he", "she" , "him"}
#print(count_words(dict))


#dict = {'word' : str, 'number': int}
#def count_words(dict):
  #  for words in dict:
   #     if 'word' not in dict:
    #        dict['number'] = 1
     #   else:
      #      dict['number'] = 1 + len.dict

#dict = {"he", "she" , "him"}
#print(count_words(dict))



#def average_prices():

def count_words(words):
    number_of_words = {}
    for word in words:
        if word in number_of_words:
            number_of_words[word] += 1
        else:
            number_of_words[word] = 1
    return number_of_words

number_of_words = {"he", "she" , "him"}

def average_prices(prices):
    total = {}
    count = {}
    for items, price in prices:
        total[items] = total.get(items, 0) + price
        count[items] = count.get(items, 0) + 1
    return {item: total[item] / count[item] for item in total}


def count_bigrams(words):
    bigram_count = {}
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        bigram_count[bigram] = bigram_count.get(bigram, 0) + 1
    return bigram_count