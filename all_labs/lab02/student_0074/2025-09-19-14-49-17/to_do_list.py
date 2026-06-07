# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

to_do_list = []

def add_task(to_do_list,a_task):
    to_do_list.append(a_task)
    l = len(to_do_list)
    return print("Task successfully added.", l ,"tasks remaining.")

def delete_task(to_do_list,d_task):
    to_do_list.remove(d_task)
    l = len(to_do_list)
    return print("Task successfully deleted.", l ,"tasks remaining.")

def move_task(to_do_list, from_index, to_index):
    task = to_do_list.pop(from_index)
    to_do_list.insert(to_index, task)
    return print("Task",task,"successfully moved to",to_index)

