# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

# This is a starting example. You do NOT need to modify this function
def clear_tasks(list):
  list.clear()

# Create an empty list
to_do_list = []

# Below please implement the add_task, delete_task, and move_task functions
# ----- YOUR CODE STARTS HERE -----
def add_task(list, task):
  list.append(task)
  N = len(list)
  return "Task successfully added. " + str(N) + " tasks remaining."

def delete_task(list, task):
  list.remove(task)
  N = len(list)
  return "Task successfully deleted. " + str(N) + " tasks remaining."

def move_task(list, from_index, to_index):
  T = list.pop(from_index)
  list.insert(to_index, T)
  return "Task '" + T + "' successfully moved to index " + str(to_index) +" "

# ===== YOUR CODE ENDS HERE =====

# You can use the code below to help test your functions

print(move_task(['Task 1', 'Task 2', 'Task 3'], 1, 0))
