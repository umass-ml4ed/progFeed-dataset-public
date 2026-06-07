# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

to_do_list = []

def add_task(lst: list, task: str):
  lst.append(task)
  number_of_tasks = len(lst)
  x = str(number_of_tasks)
  y = "Task successfully added. " + x + " tasks remaining."
  return y

def delete_task(lst: list, task: str):
  lst.remove(task)
  number_of_tasks = len(lst)
  x = str(number_of_tasks)
  y = "Task successfully deleted. " + x + " tasks remaining."
  return y

def move_task(list: list, from_index: int, to_index: int):
  x_item = list[from_index]
  list.insert(to_index, x_item)
  sto_index = str(to_index)
  sx_item = str(x_item)
  y = "Task '" + sx_item + "' successfully moved to index " + sto_index
  return y

to_do_list = ['zybook reading', 'do laundry', 'cics110 lab 3', 'math homework', 'grocery shopping']
print(move_task(['Task 1', 'Task 2', 'Task 3'], 1, 0))