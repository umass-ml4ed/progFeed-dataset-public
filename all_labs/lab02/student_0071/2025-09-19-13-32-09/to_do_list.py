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
    num_tasks = len(to_do_list)
    return f"Task successfully added. {num_tasks} tasks remaining."
my_to_do_list = []
print (add_task(my_to_do_list, "Study for math"))
print (add_task(my_to_do_list, "Read for sociology"))
print (add_task(my_to_do_list, "Dinner with Aunt"))

def delete_task(to_do_list, task):
    to_do_list.remove(task)
    num_tasks = len(to_do_list)
    return f"Task successfully deleted. {num_tasks} tasks remaining."
my_to_do_list = ["study for math", "read for sociology", "dinner with aunt"]
print(delete_task(my_to_do_list, 'study for math'))
print(delete_task(my_to_do_list, 'read for sociology'))

def move_task(to_do_list, from_index, to_index):
    task = to_do_list [from_index]
    to_do_list.pop(from_index)
    to_do_list.insert(to_index, task)
    return f"Task '{task}' successfully moved to index {to_index}"
my_to_do_list = ["study", "read", "dinner"]
print (move_task (my_to_do_list, 1,2))
print (my_to_do_list)
print(move_task (my_to_do_list, 1, 0))
print (my_to_do_list)
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
