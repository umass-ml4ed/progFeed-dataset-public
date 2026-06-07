def most_frequent_element(lst):
    if not lst:  # Handle empty list
        return None

    counts = {}  # Dictionary to store frequency of each element
    for item in lst:
        counts[item] = counts.get(item, 0) + 1

    # Find the element with the maximum frequency
    most_frequent = max(counts, key=counts.get)
    return most_frequent



def greet_user(users, user_id, default_lang="en", default_age=18):
    # Check if user exists
    if user_id not in users:
        return "User not found."

    user_info = users[user_id]
    name = user_info.get("name", "User")
    language = user_info.get("language", default_lang)
    age = user_info.get("age", default_age)

    # Define greetings
    greetings = {
        "en": {"adult": "Hello, {name}!", "child": "Hey there, {name}!"},
        "es": {"adult": "Hola, {name}!", "child": "¡Hola, pequeño/a {name}!"},
        "fr": {"adult": "Bonjour, {name}!", "child": "Salut, {name}!"}
    }

    # Use adult or child greeting
    if age < 18:
        greeting_type = "child"
    else:
        greeting_type = "adult"

    # Use greeting in user's language, fallback to English if language unknown
    language_greetings = greetings.get(language, greetings["en"])
    greeting = language_greetings[greeting_type].format(name=name)

    return greeting