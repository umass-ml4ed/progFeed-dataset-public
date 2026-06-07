# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def getnames(firstnames, lastnames):
    """
    Generates all full name combinations from lists of first and last names.

    Args:
        firstnames (list): List of first names.
        lastnames (list): List of last names.

    Returns:
        list: List of full names.
    """
    return [f"{first} {last}" for first in firstnames for last in lastnames]
