# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def most_frequent_element(input_list):
  if not input_list:
    return None

  element_counts = {}
  for element in input_list:
    element_counts[element] = element_counts.get(element, 0) + 1

  most_frequent = None
  max_count = -1

  for element, count in element_counts.items():
    if count > max_count:
      max_count = count
      most_frequent = element

  return most_frequent


def greet_user(users, user_id, default_lang="en", default_age=18):
  if user_id not in users:
    return "User not found."

  user_info = users[user_id]
  name = user_info.get("name", "User")
  language = user_info.get("language", default_lang)
  age = user_info.get("age", default_age)

  greetings = {
      "en": {"adult": "Hello, {name}!", "child": "Hey there, {name}!"},
      "es": {"adult": "Hola, {name}!", "child": "¡Hola, pequeño/a {name}!"},
      "fr": {"adult": "Bonjour, {name}!", "child": "Salut, {name}!"}
  }

  age_group = "child" if age < 18 else "adult"

  if language not in greetings:
      language = default_lang

  return greetings[language][age_group].format(name=name)