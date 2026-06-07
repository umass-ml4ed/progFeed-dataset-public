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

def add_task(list, task):
  list.append(task)
  return f"Task successfully added. {len(list)} tasks remaining."


def delete_task(list, task):
  list.remove(task)
  return f"Task successfully deleted. {len(list)} tasks remaining." 

def move_task(list, from_index, to_index):
  task = list.pop(from_index)
  list.insert(to_index, task)
  return f"Task '{task}' successfully moved to index {to_index}"




  

















  
 



  

  





  

  
  





  
  






# ===== YOUR CODE ENDS HERE =====

# You can use the code below to help test your functions

# Uncomment the following 5 lines (i.e. remove the # characters on each line) to test add_task
# (add_task(to_do_list, 'zybook reading'))
add_task(to_do_list, 'do laundry')
add_task(to_do_list, 'cics110 lab 3')
add_task(to_do_list, 'math homework')
add_task(to_do_list, 'grocery shopping')
add_task(to_do_list, 'zybook reading')
print('Current to-do list after adding tasks:', to_do_list, '/n')

# Uncomment the following 2 lines (i.e. remove the # characters on each line) to test delete_task# print(delete_task(to_do_list, 'zybook reading'))
delete_task(to_do_list, 'math homework')
delete_task(to_do_list, 'grocery shopping')
print('Current to-do list after adding tasks:', to_do_list, '/n')


# Uncomment the following 5 lines (i.e. remove the # characters on each line) to test move_task
move_task(to_do_list, 2, 0)
print('Current to-do list:', to_do_list)
