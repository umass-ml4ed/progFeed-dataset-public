#Author   : REDACTED
#Email    : REDACTED
#Spire ID : REDACTED

def clear_tasks(to_do_list):
  to_do_list.clear()

to_do_list = []

def add_task(to_do_list, task):
    to_do_list.append(task)
    N = len(to_do_list)
    return f"Task successfully added. {N} tasks remaining."

to_do_list = []

def delete_task(to_do_list, task):
   to_do_list.remove(task)
   N = len(to_do_list)
   return f"Task successfully deleted. {N} tasks remaining."

to_do_list = []

def move_task(to_do_list, task):
   to_do_list.pop(task)
   to_do_list.insert(task)
   T = len(to_do_list)
   J = len(to_do_list)
   return f"Task {T} suceessfully moved to index {J}"