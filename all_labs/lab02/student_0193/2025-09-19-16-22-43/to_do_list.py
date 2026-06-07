# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

to_do_list = []

def add_task(lst: list, task: str):
  lst.append(task)
  number_of_tasks = len(lst)
  x = str(number_of_tasks)
  return("Task succesfully completed. " + x + " tasks remaining.")

print(add_task(to_do_list, 'apple'))
print(add_task(to_do_list, 'banana'))