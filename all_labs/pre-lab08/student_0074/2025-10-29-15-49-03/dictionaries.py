# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def most_frequent_element(lis):
    if len(lis) == 0:
        return None
    
    count = {}

    for i in lis:
        if (i in count):
            count[i] = count[i] + 1
        else:
            count[i] = 1

    most_frequent = None
    highest_count = 0
    for i in count:
        if (count[i] > highest_count):
            highest_count = count[i]
            most_frequent = i

    return most_frequent

#print(most_frequent_element([3, 1, 3, 2, 3, 1, 2, 2, 2]))
# 2
#print(most_frequent_element(["apple", "banana", "apple", "orange", "banana", "apple"]))
# 'apple'
#print(most_frequent_element([1, 2, 3, 4]))
# 1, 2, 3, or 4 (any valid answer)
#print(most_frequent_element([]))
# None

def greet_user(users, user_id, default_lang="en", default_age=18):
    if (user_id not in users):
        return "User not found."

    user = users[user_id]

    if ("name" in user):
        name = user["name"]
    else:
        name = "User"

    if ("language" in user):
        lang = user["language"]
    else:
        lang = default_lang

    if ("age" in user):
        age = user["age"]
    else:
        age = default_age

    greetings = {
                "en": ("Hello, ", "Hey there, "),
                "es": ("Hola, ", "¡Hola, pequeño/a "),
                "fr": ("Bonjour, ", "Salut, ")
                }

    if (lang not in greetings):
        lang = default_lang

    adult_greet, child_greet = greetings[lang]

    if (age < 18):
        return child_greet + name + "!"
    else:
        return adult_greet + name + "!"

#users = {
#    "u1": {"name": "Alice", "language": "en", "age": 25},
 #   "u2": {"name": "Carlos", "language": "es", "age": 12},
  #  "u3": {"name": "Marie", "language": "fr"},
   # "u4": {"name": "UnknownUser"}  # Missing info
#}
#print(greet_user(users, "u1"))
# Hello, Alice!

#print(greet_user(users, "u2"))
# ¡Hola, pequeño/a Carlos!

#print(greet_user(users, "u3"))
# Bonjour, Marie!   (default_age=18 → adult greeting)

#print(greet_user(users, "u4", default_lang="es"))
# Hola, UnknownUser!   (uses default language)

#print(greet_user(users, "u5"))
# User not found.
