# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def most_frequent_element(elements):
    counts = dict()
    if elements == []:
        return None
    else:
        for element in elements:
            if element not in counts:
                counts[element] = 1
            else:
                counts[element] += 1
        largest_count = ""
        compare = 0
        for count in counts:
            if counts[count] > compare:
                compare = counts[count]
                largest_count = count
        return largest_count

def greet_user(users,user_id,default_lang = 'en', default_age = 18):
    if user_id not in users:
        return "User not found."
    if "language" not in users[user_id]:
        users[user_id]["language"] = default_lang
    if "age" not in users[user_id]:
        users[user_id]["age"] = default_age
    if users[user_id]["language"] == "en" and int(users[user_id]["age"]) >= 18:
        return (f"Hello, {users[user_id]["name"]}!")
    elif users[user_id]["language"] == "en" and int(users[user_id]["age"]) < 18:
        return(f"Hey there, {users[user_id]["name"]}!")
    elif users[user_id]["language"] == "es" and int(users[user_id]["age"]) >= 18:
        return (f"Hola, {users[user_id]["name"]}!")
    elif users[user_id]["language"] == "es" and int(users[user_id]["age"]) < 18:
        return(f"¡Hola, pequeño/a {users[user_id]["name"]}!")
    elif users[user_id]["language"] == "fr" and int(users[user_id]["age"]) >= 18:
        return(f"Bonjour, {users[user_id]["name"]}!")
    elif users[user_id]["language"] == "fr" and int(users[user_id]["age"]) < 18:
        return(f"Salut, {users[user_id]["name"]}!")
    
users = {
    "u1": {"name": "Alice", "language": "en", "age": 25},
    "u2": {"name": "Carlos", "language": "es", "age": 12},
    "u3": {"name": "Marie", "language": "fr"},
    "u4": {"name": "UnknownUser"}  # Missing info
}


print(greet_user(users, "u1"))