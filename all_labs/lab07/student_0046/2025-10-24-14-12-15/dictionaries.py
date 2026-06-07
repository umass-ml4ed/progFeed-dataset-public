# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

# 1. count_words
def count_words(words):
    """Takes a tuple of words and returns a dictionary counting occurrences."""
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


# 2. average_prices
def average_prices(prices):
    """
    Takes a tuple of (commodity, price) pairs and returns a dictionary
    with the average price for each commodity.
    """
    totals = {}
    counts = {}
    for name, price in prices:
        totals[name] = totals.get(name, 0) + price
        counts[name] = counts.get(name, 0) + 1
    return {name: totals[name] / counts[name] for name in totals}


# 3. count_bigrams
def count_bigrams(words):
    """
    Takes a tuple of words and returns a dictionary of bigram counts.
    A bigram is represented as a tuple of two consecutive words.
    """
    bigrams = {}
    for i in range(len(words) - 1):
        pair = (words[i], words[i + 1])
        if pair in bigrams:
            bigrams[pair] += 1
        else:
            bigrams[pair] = 1
    return bigrams


# ---- Test Cases ----
if __name__ == "__main__":
    # Test count_words
    words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
    print(count_words(words))  # {'he': 1, 'saw': 4, 'a': 2}

    # Test average_prices
    prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
    print(average_prices(prices))  # {'a': 1.1, 'c': 4.2, 'b': 4.0, 'd': 10.4}

    # Test count_bigrams
    words2 = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
    print(count_bigrams(words2))
    
