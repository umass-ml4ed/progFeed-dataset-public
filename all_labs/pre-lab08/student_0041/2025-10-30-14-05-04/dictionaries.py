# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def most_frequent_element(lst):
    if(lst == []):
        return None

    some_dict = {}
    for key in lst:
        if(key in some_dict):
            some_dict[key] += 1
        else:
            some_dict[key] = 1
    #return some_dict

    max_count = 0 # outside so that they don't reset every time
    max_key = ""

    for key, value in some_dict.items():
        if(max_count < value):
            max_key = key
            max_count = value
    return max_key

print(most_frequent_element([3, 1, 3, 2, 3, 1, 2, 2, 2]))
# 2

print(most_frequent_element(["apple", "banana", "apple", "orange", "banana", "apple"]))
# 'apple'

print(most_frequent_element([1, 2, 3, 4]))
# 1, 2, 3, or 4 (any valid answer)

print(most_frequent_element([]))
# None

def greet_user(users, user_id, default_lang = "en", default_age = 18):
    if(user_id not in users):
        return "User not found." # print will cause it to keep going
    else:
        user_info = users[user_id]
        # EX: {"name": "Alice", "language": "en", "age": 25}// user_id is ess. "key"

        if("name" in user_info):
            name = user_info["name"] # accesses "Alice"; the value for name
        else:
            name = "User" # default parameter

        if("language" in user_info):
            language = user_info["language"]
        else:
            language = default_lang

        if("age" in user_info):
            age = user_info["age"]
        else:
            age = default_age

        if(language == "en"):
            if(age < 18):
                greeting = "Hey there, " + str(name) + "!"
            else:
                greeting = "Hello, " + str(name) + "!"
        
        elif(language == "es"):
            if(age < 18):
                greeting = "¡Hola, pequeño/a " + str(name) + "!"
            else:
                greeting = "Hola, " + str(name) + "!"

        elif(language == "fr"):
            if(age < 18):
                greeting = "Salut, " + str(name) + "!"
            else:
                greeting = "Bonjour, " + str(name) + "!"

        else:
            greeting = "Hello, " + str(name) + "!"

    return greeting

users = {
    "u1": {"name": "Alice", "language": "en", "age": 25},
    "u2": {"name": "Carlos", "language": "es", "age": 12},
    "u3": {"name": "Marie", "language": "fr"},
    "u4": {"name": "UnknownUser"}  # Missing info
}
print(greet_user(users, "u1"))
# Hello, Alice!

print(greet_user(users, "u2"))
# ¡Hola, pequeño/a Carlos!

print(greet_user(users, "u3"))
# Bonjour, Marie!   (default_age=18 → adult greeting)

print(greet_user(users, "u4", default_lang="es"))
# Hola, UnknownUser!   (uses default language)

print(greet_user(users, "u5"))
# User not found.
