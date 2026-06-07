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


print(add_task([], "Buy groceries"))