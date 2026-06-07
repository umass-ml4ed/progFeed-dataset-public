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
