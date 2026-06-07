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
  y = "Task '" + x_item + "' successfully moved to index " + sto_index

  if from_index > to_index:
    b = from_index + 1
    del list[b]
  else:
    del list[from_index]

  return y

print(move_task(['task1', 'task2', 'task3'], 1, 0))