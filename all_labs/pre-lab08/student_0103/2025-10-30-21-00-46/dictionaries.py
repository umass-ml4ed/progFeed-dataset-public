# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def most_frequent_element(lst):
    my_dict = {}
    for i in lst:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] = my_dict[i] + 1
    for key, value in my_dict.items():
        if value == max(my_dict.values()):
            return key

def greet_user(users, user_id, default_lang = "en", default_age = 18):
    if(default_lang == "en"):
        if(default_age >= 18):
            print(f"Hello, {users[user_id]["name"]}!")
        if(default_age < 18):
            print(f"Hey there, {users[user_id]["name"]}!")
    if(default_lang == "es"):
        if(default_age >= 18):
            print(f"¡Hola, {users[user_id]["name"]}!")
        if(default_age < 18):
            print(f"¡Hola, pequeño/a {users[user_id]["name"]}!")
    if(default_lang == "fr"):
        if(default_age >= 18):
            print(f"Bonjour, {users[user_id]["name"]}!")
        if(default_age < 18):
            print(f"Salut, {users[user_id]["name"]}!")