# Authors   : REDACTED
# Emails    : REDACTED
# Spire ID REDACTED

# This is a starting example. You do NOT need to modify this function
def clear_tasks(list):
  list.clear()

# Create an empty list
to_do_list = []

# Below please implement the add_task, delete_task, and move_task functions
# ----- YOUR CODE STARTS HERE -----
def add_task(to_do_list: list, task: str) -> str:
  to_do_list.append(task)
  num_tasks = len(to_do_list)
  return(f"Task successfully added. {num_tasks} tasks remaining.")

def delete_task(to_do_list: list, task: str) -> str:
  to_do_list.remove(task)
  num_tasks = len(to_do_list)
  return(f"Task successfully deleted. {num_tasks} tasks remaining.")

def move_task(new_list: list, from_index: int, to_index: int):
  original = to_do_list[from_index]
  to_do_list.remove(original)
  to_do_list.insert(to_index, original)
  return (f"Task '{original}' succesfully moved to index {to_index}")
# ===== YOUR CODE ENDS HERE =====

# to_do_list = ['zybook reading', 'do laundry', 'cics110 lab 3']

# print(move_task(to_do_list, 2, 0))
# print(to_do_list)
# print(move_task(to_do_list, 1, 2))
# print(to_do_list)

