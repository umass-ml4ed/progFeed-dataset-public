# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def most_frequent_element(elements):
    dictionary = {}
    list_of_counts = []
    count_hosts = []
    if elements == []:
        return None
    else:
        for element in elements:
            if element not in dictionary:
                dictionary[element] = 1
            else:
                dictionary[element] += 1
        for elemental_count in dictionary:
            list_of_counts.append(dictionary[elemental_count])
            count_hosts.append(elemental_count)
        return count_hosts[list_of_counts.index(max(list_of_counts))]

def greet_user(users, user_id, default_lang="en", default_age = 18):
    if user_id not in users:
        return "User not found."
    else:
        if "language" in users[user_id]:
            default_lang = users[user_id]["language"]
        name = users[user_id]["name"]
        if "age" in users[user_id]:
            default_age = users[user_id]["age"]
        if default_lang == "es":
            if default_age >= 18:
                return f"Hola, {name}!"
            else:
                return f"¡Hola, pequeño/a {name}!"
        elif default_lang == "fr":
            if default_age >= 18:
                return f"Bonjour, {name}!"
            else:
                return f"Salut, {name}!"
        else:
            if default_age >= 18:
                return f"Hello, {name}!"
            else:
                return f"Hey there, {name}!"