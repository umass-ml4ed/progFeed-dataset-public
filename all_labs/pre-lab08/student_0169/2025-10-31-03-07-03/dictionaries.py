def most_frequent_element(elements):
    if not elements:  
        return None

    counts = {}
    for item in elements:
        counts[item] = counts.get(item, 0) + 1

    return max(counts, key=counts.get)

def greet_user(users, user_id, default_lang="en", default_age=18):
    greetings = {
        "en": {"adult": "Hello, {name}!", "child": "Hey there, {name}!"},
        "es": {"adult": "Hola, {name}!", "child": "¡Hola, pequeño/a {name}!"},
        "fr": {"adult": "Bonjour, {name}!", "child": "Salut, {name}!"},
    }

    if user_id not in users:
        return "User not found."

    user = users[user_id]

    name = user.get("name", "User")
    lang = user.get("language", default_lang)
    age = user.get("age", default_age)

    greet_type = "child" if age < 18 else "adult"

    lang_greetings = greetings.get(lang, greetings[default_lang])

    return lang_greetings[greet_type].format(name=name)
