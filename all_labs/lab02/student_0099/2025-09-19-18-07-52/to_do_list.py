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
def add_task(to_do_list, task):
  to_do_list.append(task)
  num_tasks = len(to_do_list)
  return f"Task successfully added. {num_tasks} tasks remaining."
print(add_task(to_do_list, "zybook reading"))
print(add_task(to_do_list, "do laundry"))
print(add_task(to_do_list, "cics110 lab 3"))

# ===== YOUR CODE ENDS HERE =====

