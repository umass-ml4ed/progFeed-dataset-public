# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED



   def merge_dicts(d1, d2):
    """
    Merges two dictionaries, d1 and d2, and returns a new dictionary.
    
    If a key appears in both dictionaries, its value in the result is the sum of the two values.
    
    Args:
        d1 (dict): The first dictionary to be merged.
        d2 (dict): The second dictionary to be merged.
    
    Returns:
        dict: A new dictionary that contains all keys from both d1 and d2.
    """
    result = d1.copy()  # Start with a copy of d1
    
    for key, value in d2.items():
        if key in result:
            result[key] += value  # Add the value from d2 to the existing value in the result
        else:
            result[key] = value  # Add the key-value pair from d2 to the result
    
    return result
