# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def move_task(to_do_list, from_index, to_index):
    task = to_do_list [from_index]
    to_do_list.pop(from_index)
    to_do_list.insert(to_index, task)
    return f"Task '{task}' successfully moved to index {to_index}"
my_to_do_list = ["study", "read", "dinner"]
print (move_task (my_to_do_list, 1,2))
print (my_to_do_list)
print(move_task (my_to_do_list, 1, 0))
print (my_to_do_list)