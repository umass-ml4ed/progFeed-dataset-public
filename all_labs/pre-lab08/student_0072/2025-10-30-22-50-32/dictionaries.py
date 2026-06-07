def most_frequent_element(lst):
    if not lst:
        return None
    d = {}
    for item in lst:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    max_item = None
    max_count = 0
    for item in d:
        if d[item] > max_count:
            max_count = d[item]
            max_item = item
    return max_item


def greet_user(users, user_id, default_lang="en", default_age=18):
    if user_id not in users:
        return "User not found."
    user = users[user_id]
    name = user.get("name", "User")
    lang = user.get("language", default_lang)
    age = user.get("age", default_age)
    if lang == "en":
        if age < 18:
            return f"Hey there, {name}!"
        else:
            return f"Hello, {name}!"
    elif lang == "es":
        if age < 18:
            return f"¡Hola, pequeño/a {name}!"
        else:
            return f"Hola, {name}!"
    elif lang == "fr":
        if age < 18:
            return f"Salut, {name}!"
        else:
            return f"Bonjour, {name}!"
    else:
        if age < 18:
            return f"Hey there, {name}!"
        else:
            return f"Hello, {name}!"
