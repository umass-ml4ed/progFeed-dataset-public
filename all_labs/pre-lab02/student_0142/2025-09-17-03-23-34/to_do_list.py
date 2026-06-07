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

#implement add_task
def add_task(to_do_list,task):
  to_do_list.append(task)
  #total number of tasks after adding
  num_tasks = len(to_do_list)
  return(f'Task successfully added. {num_tasks} tasks remaining.')
print(add_task(to_do_list, 'zybook reading'))
print(add_task(to_do_list,'do laundry'))
print(add_task(to_do_list, 'cics110 lab 3'))
print(add_task(to_do_list, 'math homework'))
print(add_task(to_do_list, 'grocery shopping'))


#implement delete_task
def delete_task(to_do_list,task):
  to_do_list.remove(task)
  #total number of tasks after deleting
  num_tasks = len(to_do_list)
  return(f'Task successfully deleted. {num_tasks} tasks remaining.')

to_do_list= [ 'zybook_reading','math_homework','do laudry']
print(delete_task(to_do_list, 'zybook_reading'))
print(delete_task(to_do_list, 'math_homework'))
print(delete_task(to_do_list,'do laudry'))


#implement move_task
def move_task(to_do_list,from_index, to_index):
  #remove the task from its current position
  task = to_do_list.pop(from_index)
  #insert the task at new position
  to_do_list.insert(to_index,task)
  return(f'Task {task} successfully moved to index {to_index}')

to_do_list = ['zybook reading', 'do laundry', 'cics110 lab 3', 'math homework', 'grocery shopping']
print(move_task(to_do_list, 2, 0))
print('Current to-do list:', to_do_list, '\n')
print(move_task(to_do_list, 1, 4))
print('Current to-do list:', to_do_list, '\n')




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

