# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def most_frequent_element(lst):
    """
    Finds the element that appears most frequently in the given list.

    Args:
        lst (list): A list of elements (numbers, strings, or both).

    Returns:
        The element that appears most frequently in the list. If there are multiple elements with the same highest frequency, returns any one of them. If the list is empty, returns None.
    """
    if not lst:
        return None

    # Count the frequency of each element in the list
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    # Find the element with the highest frequency
    max_freq = 0
    most_frequent = None
    for item, count in freq.items():
        if count > max_freq:
            max_freq = count
            most_frequent = item

    return most_frequent




def greet_user(users, user_id, default_lang="en", default_age=18):
    """
    Greets a user based on their stored information in a nested dictionary.

    Args:
        users (dict): A nested dictionary where keys are user IDs (strings) and
            values are dictionaries with possible keys "name", "language", and "age".
        user_id (str): The ID of the user to greet.
        default_lang (str, optional): The default language to use if the user's
            language is missing. Defaults to "en".
        default_age (int, optional): The default age to use if the user's age is
            missing. Defaults to 18.

    Returns:
        str: A greeting in the user's preferred language (or the default language
            if missing). Uses a child greeting if the user's age is below 18.
            Returns "User not found." if the ID is not in the dictionary.
    """
    if user_id not in users:
        return "User not found."

    user_info = users[user_id]
    name = user_info.get("name", "UnknownUser")
    language = user_info.get("language", default_lang)
    age = user_info.get("age", default_age)

    if age < 18:
        if language == "en":
            return f"Hey there, {name}!"
        elif language == "es":
            return f"¡Hola, pequeño/a {name}!"
        elif language == "fr":
            return f"Salut, {name}!"
    else:
        if language == "en":
            return f"Hello, {name}!"
        elif language == "es":
            return f"Hola, {name}!"
        elif language == "fr":
            return f"Bonjour, {name}!"

    # If the language is not recognized, use the default language
    if language == "en":
        return f"Hello, {name}!"
    elif language == "es":
        return f"Hola, {name}!"
    elif language == "fr":
        return f"Bonjour, {name}!"
    else:
        return f"{default_lang.capitalize()}, {name}!"
