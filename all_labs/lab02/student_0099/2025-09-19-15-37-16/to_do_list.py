# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


# This is a starting example. You do NOT need to modify this function
def clear_tasks(list):
  list.clear()

# Create an empty list
to_do_list = ['wash dishes', 'cook dinner', 'clean room']

# Below please implement the add_task, delete_task, and move_task functions
# ----- YOUR CODE STARTS HERE -----
def add_task(list):
  list.add()
print(add_task(to_do_list, 'wash dishes'))
Task successfully added. 1 tasks remaining.
print(add_task(to_do_list, 'cook dinner'))
Task successfully added. 2 tasks remaining.
print(add_task)(to_do_list, 'clean room')
Task successfully added. 3 tasks remaining.

print(delete_task(to_do_list, 'wash dishes'))
Task successfully deleted. 2 tasks remaining.
print(delete_task(to_do_list, 'cook dinner'))
Task successfully deleted. 2 tasks remaining.

print(move_task(to_do_list, 2, 0))
Task 'clean room' successfully moved to index 0

print(to_do_list)
['wash dishes', 'cook dinner', 'clean room']

print(move_task(to_do_list, 1, 2))
Task 'cook dinner' successfully moved to index 2

print(to_do_list)
['clean room', 'cook dinner', 'wash dishes']

# ===== YOUR CODE ENDS HERE =====

