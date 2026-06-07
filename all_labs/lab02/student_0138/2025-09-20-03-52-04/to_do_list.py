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

def add_task(to_do_list,description):
  to_do_list.append(description)
  print("Task successfully added.",str(len(to_do_list)),'tasks remaining.')


def delete_task(to_do_list,description):
  to_do_list.remove(description)
  print('Task successfully deleted.',str(len(to_do_list)),'tasks remaining')

def move_task(to_do_list,from_index,to_index):
  from_ = to_do_list.pop(from_index)
  to_do_list.insert(to_index, from_)
  print('Task',from_,'successfully moved to index',str(to_index))
