# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def most_frequent_element(lst:"list")-> "most common element":
    if lst == []:
        return None
    element_count = {}
    for element in lst:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1 
    for element in element_count:
        if element_count[element] == max(element_count.values()):
            return element

def greet_user(users: "nested dict", user_id, **kwargs: "dict")-> "greeting string":
    if user_id not in users:
        return "User not found."
    # setup
    user = users[user_id]
    name = user["name"]
    # defining age
    if "age" in user:
        age = user["age"]
    else:
        try:
            age = kwargs["default_age"]
        except:
            age = 18
    if age >= 18:
        str_age = "adult"
    else:
        str_age = "child"
    # defining language
    if "language" in user:
        language = user["language"]
    else:
        try:
            language = kwargs["default_language"]
        except:
            language = "en"
    # greeting
    greeting = {"en": {"adult": f"Hello, {name}!", "child": f"Hey there, {name}!"}, "es": {"adult": f"Hola, {name}!", "child": f"¡Hola, pequeño/a {name}!"}, "fr": {"adult": f"Bonjour, {name}!", "child": f"Salut, {name}!"}}
    return greeting[language][str_age]

# i need a nap