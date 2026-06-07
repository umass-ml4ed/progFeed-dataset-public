# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


# This is a starting example. You do NOT need to modify this function
def clear_tasks(list):
  list.clear()

# Create an empty list
to_do_list = ['zybook reading', 'do laundry', 'cics110 lab 3', 'math homework', 'grocery shopping']

# Below please implement the add_task, delete_task, and move_task functions
# ----- YOUR CODE STARTS HERE -----



def move_task(lst: to_do_list, from_index:int, to_index:int):
   T= to_do_list.pop(from_index)
   J= str(to_index)
   to_do_list.insert(to_index, T)
   return "Task " + str(T) + " successfully moved to index " + J





# ===== YOUR CODE ENDS HERE =====

# You can use the code below to help test your functions

# Uncomment the following 5 lines (i.e. remove the # characters on each line) to test add_task
# print(add_task(to_do_list, 'zybook reading'))
# print(add_task(to_do_list, 'do laundry'))
# print(add_task(to_do_list, 'cics110 lab 3'))
# print(add_task(to_do_list, 'math homework'))
# print(add_task(to_do_list, 'grocery shopping'))

# Uncomment the following 2 lines (i.e. remove the # characters on each line) to test delete_task
#print(delete_task(to_do_list, 'zybook reading'))
#print(delete_task(to_do_list, 'math homework'))

# Uncomment the following 5 lines (i.e. remove the # characters on each line) to test move_task
print(move_task(to_do_list, 2, 0))
print('Current to-do list:', to_do_list, '\n')
print(move_task(to_do_list, 1, 4))
print('Current to-do list:', to_do_list, '\n')
