# dictionaries.py

def count_words(words_tuple):
    """
    Count the frequency of each word in the input tuple.

    Parameters:
        words_tuple (tuple): A tuple of lower-case strings (words)

    Returns:
        dict: A dictionary where keys are unique words and values are their frequencies
    """
    word_counts = {}  # create an empty dictionary

    for word in words_tuple:
        if word in word_counts:
            word_counts[word] += 1  # increment if word already exists
        else:
            word_counts[word] = 1   # first occurrence

    return word_counts

# dictionaries.py

def average_prices(commodities):
    """
    Calculate the average price of each unique commodity.

    Parameters:
        commodities (tuple): A tuple of 2-element tuples (commodity_name, price)

    Returns:
        dict: A dictionary where keys are unique commodity names and values are average prices
    """
    total_prices = {}  # total price per commodity
    counts = {}        # count per commodity

    for name, price in commodities:
        if name in total_prices:
            total_prices[name] += price
            counts[name] += 1
        else:
            total_prices[name] = price
            counts[name] = 1

    # compute averages
    avg_prices = {name: total_prices[name] / counts[name] for name in total_prices}

    return avg_prices

# dictionaries.py

def count_bigrams(words):
    """
    Count the frequency of bigrams (pairs of consecutive words) in the input tuple.

    Parameters:
        words (tuple): A tuple of lower-case strings (individual words)

    Returns:
        dict: A dictionary where keys are bigrams (tuples of two words) and values are their frequencies
    """
    bigram_counts = {}  # empty dictionary to store bigram frequencies

    for i in range(len(words)-1):
        bigram = (words[i], words[i + 1])
        if bigram in bigram_counts:
            bigram_counts[bigram] += 1
        else:
            bigram_counts[bigram] = 1

    return bigram_counts




if __name__ == "__main__":
    # Example usage
    sample_tuple = ("apple", "banana", "apple", "orange", "banana", "apple")
    print(count_words(sample_tuple))  # Output: {'apple': 3, 'banana': 2, 'orange': 1}
    sample_commodities = (("apple", 1.0), ("banana", 0.5), ("apple", 1.2), ("orange", 0.8), ("banana", 0.6))
    print(average_prices(sample_commodities))  # Output: {'apple': 1.1, 'banana': 0.55, 'orange': 0.8}
    sample_words = ("the", "cat", "sat", "on", "the", "mat", "the", "cat")
    print(count_bigrams(sample_words))  # Output: {('the', 'cat'): 2, ('cat', 'sat'): 1, ('sat', 'on'): 1, ('on', 'the'): 1, ('the', 'mat'): 1}