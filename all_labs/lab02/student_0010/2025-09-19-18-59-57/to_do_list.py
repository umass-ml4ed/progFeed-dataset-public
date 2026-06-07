# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


# This is a starting example. You do NOT need to modify this function
def clear_tasks(list):
  list.clear()

# Create an empty list
to_do_list = ['string', 'yes', 1]

# Below please implement the add_task, delete_task, and move_task functions
# ----- YOUR CODE STARTS HERE -----
def add_task(a, b):
  a.append(b)
  c = str(len(to_do_list))
  return("Task successfully added. " + c + " tasks remaining.")
print(add_task(to_do_list, 'yes' ))

def delete_task(a, b):
  a.remove(b)
  c = str(len(to_do_list))
  return("Task successfully deleted. " + c + " tasks remaining.")
print(delete_task(to_do_list, 'yes' ))

def move_task(list, from_index, to_index):
  a = list[from_index]
  list[to_index] = a
  list.pop(from_index)
  return ("Task '" + a + "'" + ' successfully moved to index ' + str(to_index))
print(move_task(to_do_list, 0, 1))

  
  

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
