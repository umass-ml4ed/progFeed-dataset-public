# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

# def count_words(words):
#     new={}
#     for i in words:
#         if i in new:
#             new[i]+=1
#         else:
#             new[i]=1
#     return new

# def average_prices(prices):
#     total_prices = {}
#     counts = {}
#     for commodity, price in prices:
#         if commodity in total_prices:
#             total_prices[commodity] += price
#             counts[commodity] += 1
#         else:
#             total_prices[commodity] = price
#             counts[commodity] = 1
#     averages = {commodity: total_prices[commodity] / counts[commodity] for commodity in total_prices}
    
#     return averages

# def count_bigrams(words):
#     bigram_counts = {}
#     for i in range(len(words) - 1):
#         bigram = (words[i], words[i + 1])
#         if bigram in bigram_counts:
#             bigram_counts[bigram] += 1
#         else:
#             bigram_counts[bigram] = 1
#     return bigram_counts

def most_frequent_element(lst):
    if not lst:
        return None
    
    frequency = {}

    for item in lst:
        frequency[item] = frequency.get(item, 0) + 1

    most_frequent = max(frequency, key=frequency.get)
    return most_frequent

def greet_user(users, user_id, default_lang="en", default_age=18):

    if user_id not in users:
        return "User not found."

    user_info = users[user_id]

    name = user_info.get("name")
    lang = user_info.get("language", default_lang)
    age = user_info.get("age", default_age)

    greetings = {
        "en": ("Hello", "Hey there, "),
        "es": ("Hola", "¡Hola, pequeño/a!"), 
        "fr": ("Bonjour", "Salut")
    }

    greet_adult, greet_child = greetings.get(lang, greetings["en"])

    if age < 18:
        greeting = f"{greet_child} {name}!"
    else:
        greeting = f"{greet_adult} {name}!"

    return greeting
users = {
    "u1": {"name": "Alice", "language": "en", "age": 25},
    "u2": {"name": "Carlos", "language": "es", "age": 12},
    "u3": {"name": "Marie", "language": "fr"},
    "u4": {"name": "UnknownUser"}  # Missing info
}
