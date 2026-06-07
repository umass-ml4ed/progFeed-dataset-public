# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def add_task(to_do_list, task):
    to_do_list.append(task)
    num_tasks = len(to_do_list)
    return f"Task successfully added. {num_tasks} tasks remaining."
my_to_do_list = []
print (add_task(my_to_do_list, "Study for math"))
print (add_task(my_to_do_list, "Read for sociology"))
print (add_task(my_to_do_list, "Dinner with Aunt"))