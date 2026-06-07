# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def most_frequent_element(lst_of_elements):
    seen = {}
    if lst_of_elements == []:
        return None
    for element in lst_of_elements:
        if element not in seen:
            seen[element] = 1
        else:
            seen[element] += 1
    highest_value = 0
    key_with_largest_count = ""
    for key, value in seen.items():
        if value > highest_value:
            highest_value = value
            key_with_largest_count = key
    return key_with_largest_count

def greet_user(users, user_id, default_lang = "en", default_age = 18):
    if user_id not in users:
        return "User not found."
    information = users[user_id]
    if "name" in information:
        name = information["name"]
    if "language" in information:
        language = information["language"]
    else:
        language = default_lang
    if "age" in information:
        age = information["age"]
    else:
        age = default_age
    greetings = {"en": {"adult": f"Hello, {name}!", "child": f"Hey there, {name}!"}, "es": {"adult": f"Hola, {name}!", "child": f"¡Hola, pequeño/a {name}!"}, "fr": {"adult": f"Bonjour, {name}!", "child": "Salut, {name}!"}}
    if age < 18:
        group = "child"
    else:
        group = "adult"
    if language in greetings:
        return greetings[language][group]
    else:
        return greetings["en"][group]


