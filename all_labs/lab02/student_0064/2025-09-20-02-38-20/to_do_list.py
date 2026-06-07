# Author  : REDACTED
# Email : REDACTED
# Spire ID  : REDACTED


# This is a starting example. You do NOT need to modify this function
def clear_tasks(list):
  list.clear()

# Create an empty list
to_do_list = []

# Below please implement the add_task, delete_task, and move_task functions
# ----- YOUR CODE STARTS HERE -----
len(to_do_list)

def add_task(list, what_task):
  to_do_list.append(what_task)
  add_acknowledgement = "Task succesfully added. " + str(len(to_do_list)) + " takes remaining."
  return add_acknowledgement

def delete_task(list, delete_dat):
  to_do_list.remove(delete_dat)
  delete_acknowledgement = "Task succesfully deleted. " + str(len(to_do_list)) + " takes remaining."
  return delete_acknowledgement

def move_task(todo_list, from_index, to_index):
    fptask = todo_list.pop(from_index) 
    todo_list.insert(to_index, fptask) 
    move_acknowledgement = "Task '" + fptask + "' successfully moved to index " + str(to_index)
    return move_acknowledgement


# ===== YOUR CODE ENDS HERE =====

# You can use the code below to help test your functions

# Uncomment the following 5 lines (i.e. remove the # characters on each line) to test add_task
print(add_task(to_do_list, 'zybook reading'))
print(add_task(to_do_list, 'do laundry'))
print(add_task(to_do_list, 'cics110 lab 3'))
print(add_task(to_do_list, 'math homework'))
print(add_task(to_do_list, 'grocery shopping'))

# Uncomment the following 2 lines (i.e. remove the # characters on each line) to test delete_task
print(delete_task(to_do_list, 'zybook reading'))
print(delete_task(to_do_list, 'math homework'))

# Uncomment the following 5 lines (i.e. remove the # characters on each line) to test move_task
to_do_list = ['zybook reading', 'do laundry', 'cics110 lab 3', 'math homework', 'grocery shopping']
print(move_task(to_do_list, 2, 0))
print('Current to-do list:', to_do_list, '\n')
print(move_task(to_do_list, 1, 4))
print('Current to-do list:', to_do_list, '\n')
