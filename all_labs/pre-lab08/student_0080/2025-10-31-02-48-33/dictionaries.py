# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def most_frequent_element(lst):
    if not lst:
        return None
    
    count_dict = {}
    for element in lst:
        count_dict[element] = count_dict.get(element, 0) + 1
    
    max_count = 0
    most_frequent = None
    for element, count in count_dict.items():
        if count > max_count:
            max_count = count
            most_frequent = element
    
    return most_frequent

def greet_user(users, user_id, default_lang="en", default_age=18):
    if user_id not in users:
        return "User not found."
    
    user = users[user_id]
    name = user.get("name", "UnknownUser")
    language = user.get("language", default_lang)
    age = user.get("age", default_age)
    
    greetings = {
        "en": {
            "adult": "Hello, {name}!",
            "child": "Hey there, {name}!"
        },
        "es": {
            "adult": "Hola, {name}!",
            "child": "¡Hola, pequeño/a {name}!"
        },
        "fr": {
            "adult": "Bonjour, {name}!",
            "child": "Salut, {name}!"
        }
    }
    
    if language not in greetings:
        language = default_lang
    
    greeting_type = "child" if age < 18 else "adult"
    greeting_template = greetings[language][greeting_type]
    
    return greeting_template.format(name=name)


if __name__ == "__main__":
    print(most_frequent_element([3, 1, 3, 2, 3, 1, 2, 2, 2]))  
    print(most_frequent_element(["apple", "banana", "apple", "orange", "banana", "apple"])) 
    print(most_frequent_element([1, 2, 3, 4]))  
    print(most_frequent_element([])) 
    
else:
    users = {"u1": {"name": "Alice", "language": "en", "age": 25},
        "u2": {"name": "Carlos", "language": "es", "age": 12},
        "u3": {"name": "Marie", "language": "fr"},
        "u4": {"name": "UnknownUser"}}
    print(greet_user(users, "u1"))  
    print(greet_user(users, "u2")) 
    print(greet_user(users, "u3"))  
    print(greet_user(users, "u4", default_lang="es"))  
    print(greet_user(users, "u5")) 