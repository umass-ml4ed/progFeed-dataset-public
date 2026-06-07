# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def most_frequent_element(elements):
    the_dict = {item: elements.count(item) for item in elements}
    max_value = 0
    max_key = None
    for key in the_dict:
        try:
            if the_dict[key] > max_value:
                max_value = the_dict[key]
                max_key = key
        except UnboundLocalError:
            max_key
    return max_key

def greet_user(users, user_id, default_lang = 'en', default_age = 18):
    try:
        the_user = users[user_id]
    except KeyError:
        return 'User not found.'
    try:
        lang = the_user['language']
    except KeyError:
        lang = default_lang
    try:
        age = the_user['age']
    except KeyError:
        age = default_age
    if lang == 'en':
        if age < 18:
            return f"Hey there, {the_user['name']}!"
        else:
            return f"Hello, {the_user['name']}!"
    elif lang == 'es':
        if age < 18:
            return f"¡Hola, pequeño/a {the_user['name']}!"
        else:
            return f"Hola, {the_user['name']}!"
    elif lang == 'fr':
        if age < 18:
            return f"Salut, {the_user['name']}!"
        else:
            return f"Bonjour, {the_user['name']}!"