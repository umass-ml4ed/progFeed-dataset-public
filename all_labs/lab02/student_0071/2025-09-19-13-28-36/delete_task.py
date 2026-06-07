# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def delete_task(to_do_list, task):
    to_do_list.remove(task)
    num_tasks = len(to_do_list)
    return f"Task successfully deleted. {num_tasks} tasks remaining."
my_to_do_list = ["study for math", "read for sociology", "dinner with aunt"]
print(delete_task(my_to_do_list, 'study for math'))
print(delete_task(my_to_do_list, 'read for sociology'))