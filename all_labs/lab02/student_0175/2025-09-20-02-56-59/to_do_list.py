# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

to_do_list = []

def add_task(to_do_list, task):
    to_do_list.append(task)
    return f"Task successfully added. {len(to_do_list)} tasks remaining."

def delete_task(to_do_list, task):
    to_do_list.remove(task)
    return f"Task successfully deleted. {len(to_do_list)} tasks remaining."

def move_task(to_do_list, from_index, to_index):
    task = to_do_list.pop(from_index)
    to_do_list.insert(to_index, task)
    return f"Task '{task}' successfully moved to index {to_index}"
