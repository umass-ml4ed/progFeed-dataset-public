# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def get_names(first_names, last_names):
    """
    Takes two lists of strings, one for first names and one for last names,
    and returns a new list containing all combinations of first and last names.
    
    Args:
        first_names (list): A list of first names (given names).
        last_names (list): A list of last names (surnames).
    
    Returns:
        list: A list of full names, where each full name is a string
        consisting of a first name and a last name separated by a space.
    """
    full_names = []
    
    # Iterate over the first names and last names, and generate all combinations
    for first_name in first_names:
        for last_name in last_names:
            full_name = f"{first_name} {last_name}"
            full_names.append(full_name)
    
    return full_names
