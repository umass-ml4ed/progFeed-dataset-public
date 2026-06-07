# Author : REDACTED
# Email  : REDACTED
# Spire ID : REDACTED

# 1. count_words
def count_words(words):
    """
    Takes a tuple of strings (words) as input and returns
    a dictionary mapping each unique word to its count.
    """
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


# 2. average_prices
def average_prices(prices):
    """
    Takes a tuple of (commodity, price) pairs and returns a dictionary
    mapping each unique commodity to its average price.
    """
    total_prices = {}
    counts = {}

    for item, price in prices:
        if item in total_prices:
            total_prices[item] += price
            counts[item] += 1
        else:
            total_prices[item] = price
            counts[item] = 1

    avg_prices = {}
    for item in total_prices:
        avg_prices[item] = round(total_prices[item] / counts[item], 1)

    return avg_prices


# 3. count_bigrams
def count_bigrams(words):
    """
    Takes a tuple of strings (words) as input and returns
    a dictionary mapping each unique bigram (pair of consecutive words)
    to its count.
    """
    bigram_counts = {}
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        if bigram in bigram_counts:
            bigram_counts[bigram] += 1
        else:
            bigram_counts[bigram] = 1
    return bigram_counts


# -----------------------------
# Test cases (for you to verify)
# -----------------------------
if __name__ == "__main__":
    # Test 1: count_words
    words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
    print(count_words(words))
    # Expected: {'he': 1, 'saw': 4, 'a': 2}

    # Test 2: average_prices
    prices = (('a', 1.0), ('c', 4.2), ('b', 3.9),
              ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
    print(average_prices(prices))
    # Expected: {'a': 1.1, 'c': 4.2, 'b': 4.0, 'd': 10.4}

    # Test 3: count_bigrams
    words = ('she', 'knows', 'and', 'she', 'knows', 'that',
             'he', 'knows', 'that', 'she', 'knows')
    print(count_bigrams(words))
    # Expected: {('she', 'knows'): 3, ('knows', 'and'): 1, ('and', 'she'): 1,
    #            ('knows', 'that'): 2, ('that', 'he'): 1, ('he', 'knows'): 1,
    #            ('that', 'she'): 1}
