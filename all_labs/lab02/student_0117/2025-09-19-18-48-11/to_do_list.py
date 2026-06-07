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
tasks_count = 0

#add_task Code
def add_task(which_task_being_added: list, description_of_task: str):
  which_task_being_added.append(str(description_of_task))
  return ("Task successfully added. " + str(len(which_task_being_added)) + " tasks remaining.")

#delete_task Code
def delete_task(task_being_modified: list, desciption_of_the_task: str):
  task_being_modified.pop(task_being_modified.index(str(desciption_of_the_task)))
  return "Task successfully deleted. " + str(len(task_being_modified)) + " tasks remaining."


def move_task(task_that_will_modified: list, from_index: int, to_index: int):
    popped_item = task_that_will_modified.pop(from_index)
    task_that_will_modified.insert(to_index, popped_item)
    return f"Task '{popped_item}' successfully moved to index {to_index}."

#move_task Code
#def move_task(task_that_will_modified: list, from_index: int, to_index: int):
  #task_that_will_modified.insert(to_index, popped_item)
  #return f"Task '{popped_item}' successfully moved to index {to_index}."


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

print(delete_task(['Buy groceries', 'Clean the house', 'Finish homework'], 'Finish homework'))

print(move_task(['Task 1', 'Task 2', 'Task 3'], 1, 0))