#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

import random

def most_frequent_element(lst: list): 
    if lst == []:
        return None
    frequencies = {}
    same_frequency = []
    winner = 'dummy'
    for element in lst:
        if element in frequencies:
            frequencies[element] += 1
        else:
            frequencies[element] = 1
    for element in frequencies:
        if winner == 'dummy':
            winner = element
        elif frequencies[element] > frequencies[winner]:
            winner = element
        elif frequencies[element] == frequencies[winner]:
            same_frequency.append(element)
            if winner not in same_frequency:
                same_frequency.append(winner)
    if same_frequency != [] and same_frequency[0] > winner:
        return random.choice(same_frequency)
    return winner

def greet_user(users: dict, user_id: str, default_lang='en', default_age=18) -> str:
    if user_id not in users:
        return 'User not found.'
    target_user = users[user_id]
    if ('language' in target_user and target_user['language'] == 'en') or ('language' not in target_user and default_lang == 'en'):
        if default_age < 18 or ('age' in target_user and target_user['age'] < 18):
            return f'Hey there, {target_user["name"]}!'
        else:
            return f'Hello, {target_user["name"]}!'
    elif ('language' in target_user and target_user['language'] == 'es') or ('language' not in target_user and default_lang == 'es'):
        if default_age < 18 or ('age' in target_user and target_user['age'] < 18):
            return f'¡Hola, pequeño/a {target_user["name"]}!'
        else:
            return f'Hola, {target_user["name"]}!'
    elif ('language' in target_user and target_user['language'] == 'fr') or ('language' not in target_user and default_lang == 'fr'):
        if default_age < 18 or ('age' in target_user and target_user['age'] < 18):
            return f'Salut, {target_user["name"]}!'
        else:
            return f'Bonjour, {target_user["name"]}!'
    


