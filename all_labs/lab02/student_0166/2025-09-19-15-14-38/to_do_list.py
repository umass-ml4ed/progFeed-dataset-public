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
# Question 1
def add_task(to_do_list, task):
  to_do_list.append(task)
  return f'Task successfully added. {len(to_do_list)} tasks remaining.'

# ===== YOUR CODE ENDS HERE =====

print(add_task(to_do_list, 'zybook reading'))
print(add_task(to_do_list, 'do laundry'))
print(add_task(to_do_list, 'cics110 lab 3'))
print(add_task(to_do_list, 'math homework'))
print(add_task(to_do_list, 'grocery shopping'))

# Question 2
def delete_task(to_do_list, removed_task):
  to_do_list.remove(removed_task)
  return f'Task successfully deleted. {len(to_do_list)} tasks remaining.'
 
print(delete_task(to_do_list, 'zybook reading'))
print(delete_task(to_do_list, 'math homework'))

# Question 3
def move_task(to_do_list, from_index, to_index):
  task=to_do_list.pop(to_index)
  to_do_list.insert(from_index,task)
  return f'Task \'{(task)}\' successfully moved to index {(to_index)}'
 
# Uncomment the following 5 lines (i.e. remove the # characters on each line) to test move_task
to_do_list = ['zybook reading', 'do laundry', 'cics110 lab 3', 'math homework', 'grocery shopping']
print(move_task(to_do_list, 2, 0))
print('Current to-do list:', to_do_list, '\n')
print(move_task(to_do_list, 1, 4))
print('Current to-do list:', to_do_list, '\n')
