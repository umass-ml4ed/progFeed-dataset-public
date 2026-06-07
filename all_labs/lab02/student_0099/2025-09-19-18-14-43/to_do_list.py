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

def delete_task(to_do_list, task):
    to_do_list.remove(task)
    num_tasks = len(to_do_list)
    return f"Task successfully deleted. {num_tasks} tasks remaining."
to_do_list = ["zybook reading", "do laundry", "cics110 lab 3"]
print(delete_task(to_do_list, "do laundry"))
print(delete_task(to_do_list, "cics110 lab 3"))

def move_task(to_do_list, from_index, to_index):
    task = to_do_list.pop(from_index)
    to_do_list.insert(to_index, task)
    return f"Task '{task}' successfully moved to index {to_index}"
to_do_list = ['zybook reading', 'do laundry', 'cics110 lab 3']

print(move_task(to_do_list, 2, 0))
print(to_do_list)
print(move_task(to_do_list, 1, 2))
print(to_do_list)

# ===== YOUR CODE ENDS HERE =====

