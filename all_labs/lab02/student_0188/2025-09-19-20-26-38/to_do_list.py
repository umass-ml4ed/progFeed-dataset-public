# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

# This is a starting example. You do NOT need to modify this function
def clear_tasks(list):
  list.clear()

# Create an empty list
to_do_list = []

# Below please implement the add_task, delete_task, and move_task functions
# ----- YOUR CODE STARTS HERE -----

# Starter function provided
def clear_tasks(to_do_list):
    to_do_list.clear()

# 1. Add a new task to the end of the list
def add_task(to_do_list, task):
    to_do_list.append(task)
    return f"Task successfully added. {len(to_do_list)} tasks remaining."

# 2. Delete a task from the list
def delete_task(to_do_list, task):
    to_do_list.remove(task)
    return f"Task successfully deleted. {len(to_do_list)} tasks remaining."

# 3. Move a task from one index to another
def move_task(to_do_list, from_index, to_index):
    task = to_do_list.pop(from_index)
    to_do_list.insert(to_index, task)
    return f"Task '{task}' successfully moved to index {to_index}"

# ===== YOUR CODE ENDS HERE =====

# Example usage / testing
to_do_list = []

# Testing add_task
print(add_task(to_do_list, 'zybook reading'))  # Task successfully added. 1 tasks remaining.
print(add_task(to_do_list, 'do laundry'))      # Task successfully added. 2 tasks remaining.
print(add_task(to_do_list, 'cics110 lab 3'))   # Task successfully added. 3 tasks remaining.

# Testing delete_task
print(delete_task(to_do_list, 'do laundry'))   # Task successfully deleted. 2 tasks remaining.
print(delete_task(to_do_list, 'cics110 lab 3'))# Task successfully deleted. 1 tasks remaining.

# Reset list for move_task testing
to_do_list = ['zybook reading', 'do laundry', 'cics110 lab 3']
print(move_task(to_do_list, 2, 0))             # Task 'cics110 lab 3' successfully moved to index 0
print(to_do_list)                              # ['cics110 lab 3', 'zybook reading', 'do laundry']

print(move_task(to_do_list, 1, 2))             # Task 'zybook reading' successfully moved to index 2
print(to_do_list)                              # ['cics110 lab 3', 'do laundry', 'zybook reading']
