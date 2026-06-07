# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

### Code from the other dictionaries project
'''
def count_words(strings):
    words = {}
    for i in strings:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    return words

#words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
#print(count_words(words))

def average_prices(names_and_prices):
    lists_of_prices = {}
    for name_and_price in names_and_prices:
        if name_and_price[0] not in lists_of_prices:
            lists_of_prices[name_and_price[0]] = [name_and_price[1]]
        else:
            lists_of_prices[name_and_price[0]].append(name_and_price[1])
    average_price_dict = {}
    for item in lists_of_prices:
        average_price_dict[item] = (sum(lists_of_prices[item]) / len(lists_of_prices[item]))
    return average_price_dict

#prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
#print(average_prices(prices))

def count_bigrams(words):
    bigrams = {}
    for index, word in enumerate(words):
        if index == (len(words) - 1):
            break
        firstnext = (word, words[index + 1])
        if firstnext not in bigrams:
            bigrams[firstnext] = 1
        else:
            bigrams[firstnext] += 1
    return bigrams

#words = ('she', 'knows', 'and', 'she', 'knows', 'that', 'he', 'knows', 'that', 'she', 'knows')
#print(count_bigrams(words))

'''

def most_frequent_element(list):
    item_count = {}
    for i in list:
        if i in item_count:
            item_count[i] += 1
        else:
            item_count[i] = 1
    
    highest_count = 0
    most = None
    for i in item_count:
        if item_count[i] > highest_count:
            highest_count = item_count[i]
            most = i

    return most

#print(most_frequent_element([3, 1, 3, 2, 3, 1, 2, 2, 2]))
#print(most_frequent_element(["apple", "banana", "apple", "orange", "banana", "apple"]))
#print(most_frequent_element([1, 2, 3, 4]))
#print(most_frequent_element([]))

def greet_user(users, user_id, default_lang='en', default_age=18):
    if user_id not in users:
        return "User not found."
    
    if "language" in users[user_id]:
        language = users[user_id]["language"]
    else:
        language = default_lang

    if "age" in users[user_id]:
        age = users[user_id]["age"]
    else:
        age = default_age

    child = age < 18

    match (language, child):
        case ("en", False):
            return f"Hello, {users[user_id]["name"]}!"
        case ("en", True):
            return f"Hey there, {users[user_id]["name"]}!"
        case ("es", False):
            return f"Hola, {users[user_id]["name"]}!"
        case ("es", True):
            return f"¡Hola, pequeño/a {users[user_id]["name"]}!"
        case ("fr", False):
            return f"Bonjour, {users[user_id]["name"]}!"
        case ("fr", True):
            return f"Salut, {users[user_id]["name"]}!"
        
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