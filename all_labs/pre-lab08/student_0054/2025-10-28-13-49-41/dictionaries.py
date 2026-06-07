# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED



"""
Write a function, called most_frequent_element, which should:
Take a list of elements (numbers, strings, or both) as a parameter.
Return the element that appears most frequently in the list.
If there are multiple elements with the same highest frequency, return any one of them.
Hints

You can use a dictionary to count how many times each element appears.
Loop through the list and update the counts.
Then, find the key with the largest count.
Handle the case when the list is empty by returning None.
"""

def most_frequent_element(items):
    if not items:
        return None

    counts = {}
    for x in items:
        counts[x] = counts.get(x, 0) + 1

    most = None
    best = -1
    for k, v in counts.items():
        if v > best:
            most, best = k, v
    return most

# print(most_frequent_element([3, 1, 3, 2, 3, 1, 2, 2, 2]))
# # 2
#
# print(most_frequent_element(["apple", "banana", "apple", "orange", "banana", "apple"]))
# # 'apple'
#
# print(most_frequent_element([1, 2, 3, 4]))
# # 1, 2, 3, or 4 (any valid answer)
#
# print(most_frequent_element([]))
# # None


"""
Write a function that greets a user based on their stored information in a nested dictionary.
The function takes:
users: a nested dictionary where:
keys are user IDs (strings)
values are dictionaries with possible keys "name", "language", and "age"
user_id: the ID of the user to greet
default_lang: a string (default "en") that is used if the user’s language is missing
default_age: an integer (default 18) that is used if the user’s age is missing

The function should:
1. 2. Return a greeting in the user’s preferred language (or the default language if missing).
Use a child greeting if the user’s age is below 18.
3. Return "User not found.
" if the ID is not in the dictionary.
"""

def greet_user(users, user_id, default_lang="en", default_age=18):
    if user_id not in users:
        return "User not found."

    data = users[user_id]
    name = data.get("name", "UnknownUser")
    lang = data.get("language", default_lang)
    age = data.get("age", default_age)

    greetings = {
        "en": {"adult": "Hello, {name}!", "child": "Hey there, {name}!"},
        "es": {"adult": "Hola, {name}!", "child": "¡Hola, pequeño/a {name}!"},
        "fr": {"adult": "Bonjour, {name}!", "child": "Salut, {name}!"},
    }
    if lang not in greetings:
        lang = "en"

    mode = "child" if age < 18 else "adult"
    return greetings[lang][mode].format(name=name)

# users = {
#     "u1": {"name": "Alice", "language": "en", "age": 25},
#     "u2": {"name": "Carlos", "language": "es", "age": 12},
#     "u3": {"name": "Marie", "language": "fr"},
#     "u4": {"name": "UnknownUser"}  # Missing info
# }
#
# print(greet_user(users, "u1"))
# # Hello, Alice!
#
# print(greet_user(users, "u2"))
# # ¡Hola, pequeño/a Carlos!
#
# print(greet_user(users, "u3"))
# # Bonjour, Marie!   (default_age=18 → adult greeting)
#
# print(greet_user(users, "u4", default_lang="es"))
# # Hola, UnknownUser!   (uses default language)
#
# print(greet_user(users, "u5"))
# # User not found.
