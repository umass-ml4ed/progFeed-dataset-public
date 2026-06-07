# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


# This is a starting example. You do NOT need to modify this function
def clear_tasks(list):
  list.clear()

# Create an empty list
to_do_list = []

# Below please implement the add_task, delete_task, and move_task functions
# ----- YOUR CODE STARTS HERE -----

def add_task(lst: list, task: str):
  lst.append(task)
  return "Task successfully added. " + str(len(lst)) + " tasks remaining."


def delete_task(lst: list, task: str):
  lst.remove(task)
  return "Task successfully deleted. " + str(len(lst)) + " tasks remaining."

def move_task(lst: list, from_index: int, to_index: int):
  task = lst[from_index]
  lst.pop(from_index)           
  lst.insert(to_index, task)
  return "Task " + str(lst[to_index]) + " successfully moved to index " + str(to_index)



# ===== YOUR CODE ENDS HERE =====

# You can use the code below to help test your functions

# Uncomment the following 5 lines (i.e. remove the # characters on each line) to test add_task
print(add_task(to_do_list, 'zybook reading'))
print(add_task(to_do_list, 'do laundry'))
print(add_task(to_do_list, 'cics110 lab 3'))
print(add_task(to_do_list, 'math homework'))
print(add_task(to_do_list, 'grocery shopping'))
print(to_do_list)

# # # Uncomment the following 2 lines (i.e. remove the # characters on each line) to test delete_task
# print(delete_task(to_do_list, 'zybook reading'))
# print(delete_task(to_do_list, 'math homework'))
# print(to_do_list)

# Uncomment the following 5 lines (i.e. remove the # characters on each line) to test move_task
# to_do_list = ['zybook reading', 'do laundry', 'cics110 lab 3', 'math homework', 'grocery shopping']
# print(move_task(to_do_list, 2, 0))
# print('Current to-do list:', to_do_list, '\n')
# print(move_task(to_do_list, 1, 4))
# print('Current to-do list:', to_do_list, '\n')


# to_do_list = ['zybook reading', 'do laundry', 'cics110 lab 3']

# print(move_task(to_do_list, 2, 0))
# # # Task 'cics110 lab 3' successfully moved to index 0

# print(to_do_list)
# # # ['cics110 lab 3', 'zybook reading', 'do laundry']

# print(move_task(to_do_list, 1, 2))
# # # Task 'zybook reading' successfully moved to index 2

# print(to_do_list)
# # # ['cics110 lab 3', 'do laundry', 'zybook reading']
