# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

to_do_list = []



def move_task(list: list, from_index: int, to_index: int):
  x_item = list[from_index]
  list.remove(x_item)
  list.insert(to_index, x_item)
  sto_index = str(to_index)
  y = "Task '" + x_item + "' successfully moved to index " + sto_index
  return y

print(move_task(['task1', 'task2', 'task3'], 2, 0))