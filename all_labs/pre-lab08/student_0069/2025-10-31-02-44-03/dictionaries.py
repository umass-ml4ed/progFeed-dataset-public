
def most_frequent_element(elements):
    if not elements:
        return None 
    
    count_dict = {}
    for e in elements:
        if e in count_dict:
            count_dict[e] += 1
        else:
            count_dict[e] = 1
    

    max_count = 0 
    most_frquent = None 

    for e, count in count_dict.items():
        if count > max_count:
            max_count = count 
            most_frequent = e

    return most_frequent 


def greet_user(users, user_id, d_lang = "en", d_age = 18):
    if user_id not in user:
        return "User not found."
    
    user = users[user_id]

    name = user.get("name", "UnknownUser")
    lang = user.get("language", d_lang)


    age = user.get("age")
    if age is None:
        age = d_age

    greetings = {
        "en": {
            "adult": "Hello, {name}!", 
            "child" : "Hey there, {name}!"
        },
        "es": {
            "adult": "Hola {name}!",
            "child": "iHola, pequeño/a {name}!"
        
        },

        "fr": {
            "adult" : "Bonjour, {name}!",
            "child" : "Salut, {name}!" 

        }
    }

    if lang not in greetings:
        lang = d_lang 
    
    greeting_type = "child" if age < 18 else "adult"
    template = greetings[lang][greeting_type]

    return template.format(name = name )
