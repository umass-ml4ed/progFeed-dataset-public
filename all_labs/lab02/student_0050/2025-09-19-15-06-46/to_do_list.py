# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

to_do_list = []
desc = "laundry"

def clear_tasks(to_do_list):
    to_do_list.clear()

def add_task(to_do_list, desc):
    to_do_list.insert(len(to_do_list),desc)
    return f"Task successfully added. {len(to_do_list)} tasks remaining."

def delete_task(to_do_list,desc):
    to_do_list.remove(desc)
    return f"Task successfully deleted. {len(to_do_list)} tasks remaining."


def move_task(to_do_list, from_index, to_index):
    task = to_do_list.pop(from_index)
    to_do_list.insert(to_index,task)
    return f'Task {task} successfully moved to index{to_index}'



