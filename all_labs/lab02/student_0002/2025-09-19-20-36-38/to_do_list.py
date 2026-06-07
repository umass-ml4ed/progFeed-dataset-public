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
def add_task(to_do_list, task):
    to_do_list.append(task)
    print("Task successfully added. " + str(len(to_do_list)) + " tasks remaining.")
    return to_do_list

def delete_task(to_do_list, task):
   to_do_list.remove(task)
   print("Task successfully deleted. " + str(len(to_do_list)) + " tasks remaining.")
   return to_do_list

def move_task(to_do_list, from_index, to_index):
   task = to_do_list.pop(from_index)
   to_do_list.insert(to_index, task)
   print(f"Task {str(task)} successfully moved to index {str(to_index)}.")
   return to_do_list


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
to_do_list = ['zybook reading', 'do laundry', 'cics110 lab 3', 'math homework', 'grocery shopping']
print(move_task(to_do_list, 2, 0))
print('Current to-do list:', to_do_list, '\n')
print(move_task(to_do_list, 1, 4))
print('Current to-do list:', to_do_list, '\n')