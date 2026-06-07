# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
def most_frequent_element(lst):
    dct = {}
    if (len(lst) == 0):
        return  None
    else:
        for i in range (len(lst)):
            if lst[i] not in dct:
                dct[lst[i]] = 1
            else:
                dct[lst[i]] += 1
        max = 0
        for key, count in dct.items():
            if count > max:
                max = count
                max_value_item = key
        return max_value_item
def greet_user(users:dict, greet_user, default_age = 18, default_lang="en"):
        if (greet_user in users):
            dct = users[greet_user]
            age = dct.get("age", default_age)
            lang = dct.get("language", default_lang)
            # print (type(age))
            try:
                age = int(age)
            except (ValueError, TypeError):
                age = default_age
            if (lang == "en"):
                if (age >= 18):
                    return (f"Hello, {dct['name']}!")
                else:
                    return (f"Hey there, {dct['name']}!")
            elif (lang == "es"):
                if (age >= 18):
                    return (f"Hola, {dct['name']}!")
                else:
                    return (f"¡Hola, pequeño/a {dct['name']}!")
            elif (lang == "fr"):
                if (age >= 18):
                    return (f"Bonjour, {dct['name']}!")
                else:
                    return (f"¡Salut, {dct['name']}!")
            else:
                return (f"Hello, {dct['name']}!")
        else:
            return "User not found."



        