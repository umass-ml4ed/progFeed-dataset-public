# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def most_frequent_element(lst):
    if not lst:
        return None  # handle empty list

    counts = {}
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    return max(counts, key=counts.get)


def greet_user(users, user_id, default_lang="en", default_age=18):
    if user_id not in users:
        return "User not found."

    user = users[user_id]
    name = user.get("name", "User")
    lang = user.get("language", default_lang)
    age = user.get("age", default_age)

    greetings = {
        "en": ("Hello, {name}!", "Hey there, {name}!"),
        "es": ("Hola, {name}!", "¡Hola, pequeño/a {name}!"),
        "fr": ("Bonjour, {name}!", "Salut, {name}!")
    }

    adult_greet, child_greet = greetings.get(lang, greetings["en"])

    if age < 18:
        return child_greet.format(name=name)
    else:
        return adult_greet.format(name=name)


# Example tests (you can comment these out before submitting)
#if __name__ == "__main__":
    print(most_frequent_element([3, 1, 3, 2, 3, 1, 2, 2, 2]))  # 2
    print(most_frequent_element([]))  # None

    users = {
        "u1": {"name": "Alice", "language": "en", "age": 25},
        "u2": {"name": "Carlos", "language": "es", "age": 12},
        "u3": {"name": "Marie", "language": "fr"},
        "u4": {"name": "UnknownUser"}
    }

    print(greet_user(users, "u1"))  # Hello, Alice!
    print(greet_user(users, "u2"))  # ¡Hola, pequeño/a Carlos!
    print(greet_user(users, "u3"))  # Bonjour, Marie!
    print(greet_user(users, "u4", default_lang="es"))  # Hola, UnknownUser!
    print(greet_user(users, "u5"))  # User not found.



