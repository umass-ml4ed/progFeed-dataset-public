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
def add_task(to_do_list, task1):
  to_do_list.append(task1)
  return f"successfully added. {len(to_do_list)} tasks remaining"
print(add_task(to_do_list, ' do laundry'))
print(add_task(to_do_list, ' give a mouse a cookie'))
print(add_task(to_do_list, ' add two and three'))

def delete_task(to_do_list, task1):
  to_do_list.remove(task1)
  return f"sucessfully deleted. {len(to_do_list)} tasks remaining"
print(delete_task(to_do_list, ' do laundry'))
print(delete_task(to_do_list, ' give a mouse a cookie'))
print(delete_task(to_do_list, ' add two and three'))

def move_task(to_do_list, from_index, to_index, task1):
  to_do_list.pop(task1,from_index)
  to_do_list.insert(task1, to_index)
  return f"Task 'do laundry' sucessfully moved to index 0"
  
 



  

  





  

  
  





  
  






# ===== YOUR CODE ENDS HERE =====

# You can use the code below to help test your functions

# Uncomment the following 5 lines (i.e. remove the # characters on each line) to test add_task
# print(add_task(to_do_list, 'zybook reading'))
# print(add_task(to_do_list, 'do laundry'))
# print(add_task(to_do_list, 'cics110 lab 3'))
# print(add_task(to_do_list, 'math homework'))
# print(add_task(to_do_list, 'grocery shopping'))

# Uncomment the following 2 lines (i.e. remove the # characters on each line) to test delete_task
# print(delete_task(to_do_list, 'zybook reading'))
# print(delete_task(to_do_list, 'math homework'))

# Uncomment the following 5 lines (i.e. remove the # characters on each line) to test move_task
#to_do_list = ['zybook reading', 'do laundry', 'cics110 lab 3', 'math homework', 'grocery shopping']
#print(move_task(to_do_list, 2, 0))
#print('Current to-do list:', to_do_list, '\n')
#print(move_task(to_do_list, 1, 4))
#print('Current to-do list:', to_do_list, '\n')
