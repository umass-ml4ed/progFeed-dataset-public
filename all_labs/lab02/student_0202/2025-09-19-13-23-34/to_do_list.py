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
def add_task(lst, task):
  lst.append(task)
  return f"Task successfully added. {len(lst)} tasks remaining."

def delete_task(lst, task):
  lst.remove(task)
  return f"Task successfully added. {len(lst)} tasks remaining."

def move_task(lst,index1,index2):
  lst.insert(index2, lst.pop(index1))
  return f"Task {lst[index1]} successfully moved to index {index2}"

# ===== YOUR CODE ENDS HERE =====

# You can use the code below to help test your functions

print(add_task(to_do_list, 'zybook reading'))
print(add_task(to_do_list, 'do laundry'))
print(add_task(to_do_list, 'cics110 lab 3'))
print(add_task(to_do_list, 'math homework'))
print(add_task(to_do_list, 'grocery shopping'))


print(delete_task(to_do_list, 'zybook reading'))
print(delete_task(to_do_list, 'math homework'))


to_do_list = ['zybook reading', 'do laundry', 'cics110 lab 3', 'math homework', 'grocery shopping']
print(move_task(to_do_list, 2, 0))
print('Current to-do list:', to_do_list, '\n')
print(move_task(to_do_list, 1, 4))
print('Current to-do list:', to_do_list, '\n')