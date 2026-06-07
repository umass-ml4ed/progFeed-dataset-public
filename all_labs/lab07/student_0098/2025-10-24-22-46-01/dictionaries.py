# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED




def count_words(words):
    """
    Counts the frequency of words in a given tuple of words.

    Args:
        words (tuple): A tuple of strings (words).

    Returns:
        dict: A dictionary where the keys are unique words and the values are the number of occurrences of each word.
    """
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count



def average_prices(commodities):
    """
    Calculates the average prices of unique commodities.

    Args:
        commodities (tuple): A tuple of tuples, where each inner tuple contains the name of a commodity and its price.

    Returns:
        dict: A dictionary where the keys are the unique commodity names and the values are the average prices of those commodities.
    """
    # Create a dictionary to store the total price and count for each unique commodity
    price_totals = {}
    counts = {}

    # Loop through the input commodities
    for commodity, price in commodities:
        # Check if the commodity is already in the dictionaries
        if commodity in price_totals:
            price_totals[commodity] += price
            counts[commodity] += 1
        else:
            price_totals[commodity] = price
            counts[commodity] = 1

    # Calculate the average prices and return the result
    return {commodity: price_totals[commodity] / counts[commodity] for commodity in price_totals}
def count_bigrams(words):
    """
    Counts the frequency of bigrams (sequences of two adjacent words) in the given tuple of words.

    Args:
        words (tuple): A tuple of strings representing the words.

    Returns:
        dict: A dictionary where the keys are unique bigrams and the values are the counts of each bigram.
    """
    bigram_counts = {}

    # Loop through the words, creating bigrams and updating the counts
    for i in range(len(words) - 1):
        bigram = (words[i], words[i + 1])
        if bigram in bigram_counts:
            bigram_counts[bigram] += 1
        else:
            bigram_counts[bigram] = 1

    return bigram_counts
