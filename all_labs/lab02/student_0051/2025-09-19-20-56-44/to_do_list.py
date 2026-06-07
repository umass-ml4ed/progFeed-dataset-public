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
    cd = len(to_do_list)
    return "Task successfully added. " + str(cd) + " tasks remaining."
print(add_task(to_do_list, "bookstore"))

def delete_task(to_do_list, task):
    to_do_list.remove(task)
    bc = len(to_do_list)
    return "Task successfully deleted. " + str(bc) + " tasks remaining."

def move_task(to_do_list, from_index, to_index):
   task = to_do_list.pop(from_index)
   to_do_list.insert(to_index, task)
   return f"Task '{task}' successfully moved to index {to_index}"
# ===== YOUR CODE ENDS HERE =====
