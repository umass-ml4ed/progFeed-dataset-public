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
def add_task(list, to_add):
  list.append(to_add)
  tasks_remaining = len(list)
  return f"Task successfully added. {tasks_remaining} tasks remaining"

print(add_task(to_do_list, 'eat'))
print(add_task(to_do_list, 'sleep'))
print(add_task(to_do_list, 'play'))
print(add_task(to_do_list, 'rest'))
print(to_do_list)

def delete_task(list, to_delete):
  list.remove(to_delete)
  tasks_remaining = len(list)
  return f"Task successfully removed. {tasks_remaining} tasks remaining"

print(delete_task(to_do_list, 'eat'))
print(to_do_list)

def move_task(list, from_index, to_index):
  initial_index = list[to_index]
  list[to_index] = list[from_index]
  list[from_index] = initial_index
  return f"Task '{list[to_index]}' successfully moved to index {to_index}"

print(move_task(to_do_list, 0, 2))
print(to_do_list)

# ===== YOUR CODE ENDS HERE =====

# You can use the code below to help test your functions

# Uncomment the following 5 lines (i.e. remove the # characters on each line) to test add_task
#print(add_task(to_do_list, 'zybook reading'))
#print(add_task(to_do_list, 'do laundry'))
#print(add_task(to_do_list, 'cics110 lab 3'))
#print(add_task(to_do_list, 'math homework'))
#print(add_task(to_do_list, 'grocery shopping'))

# Uncomment the following 2 lines (i.e. remove the # characters on each line) to test delete_task
#print(delete_task(to_do_list, 'zybook reading'))
#print(delete_task(to_do_list, 'math homework'))

# Uncomment the following 5 lines (i.e. remove the # characters on each line) to test move_task
#to_do_list = ['zybook reading', 'do laundry', 'cics110 lab 3', 'math homework', 'grocery shopping']
#print(move_task(to_do_list, 2, 0))
#print('Current to-do list:', to_do_list, '\n')
#print(move_task(to_do_list, 1, 4))
#print('Current to-do list:', to_do_list, '\n')
