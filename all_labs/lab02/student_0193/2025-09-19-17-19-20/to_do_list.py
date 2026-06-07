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

print(add_task(to_do_list, 'zybook reading'))
print(add_task(to_do_list, 'do laundry'))
print(add_task(to_do_list, 'cics110 lab 3'))

def delete_task(lst: list, task: str):
  lst.remove(task)
  number_of_tasks = len(lst)
  x = str(number_of_tasks)
  y = "Task successfully deleted. " + x + " tasks remaining."
  return y

print(delete_task(to_do_list, 'do laundry'))
print(delete_task(to_do_list, 'cics110 lab 3'))

def move_task(list: list, from_index: int, to_index: int):
  x_item = list[from_index]
  list.insert(to_index, x_item)
  sto_index = str(to_index)
  y = "Task '" + x_item + "'successfully moved to index" + sto_index
  return y

to_do_list = ['zybook reading', 'do laundry', 'cics110 lab 3', 'math homework', 'grocery shopping']
print(move_task(to_do_list, 2, 0))
print('Current to-do list:', to_do_list, '\n')
print(move_task(to_do_list, 1, 4))
print('Current to-do list:', to_do_list, '\n')