# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_words(tuple):
        counts = {}
        for word in tuple:
                if word not in counts:
                        counts[word] = 1
                else: 
                        counts[word] += 1
        return counts 
def average_prices(tuple):
        price = {}
        for name, price in tuple:
                if name not in price:
                        price[name] = [price]
                else:
                        price[name].append(price)
        averages = {}
        for name, price in price.items():
                averages[name] = sum(price) / len(price)
        return averages
def count_bigrams(tuple): 
        counts = {}
        if len(tuple) < 2:
                return counts
        for i in range(len(tuple) - 1):
                biagram = (tuple[i], tuple(i+1))
                if biagram not in counts: 
                        counts[biagram] = 1
                else: 
                        counts[biagram] += 1
        return counts

                        
