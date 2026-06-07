# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


# This is a starting example. You do NOT need to modify this function
def clear_tasks(list):
  list.clear()

# Create an empty list
to_do_list = []


def add_task(list_to_do, task):
    list_to_do.append(task)
    N = len(list_to_do)
    return f"Task successfully added. {N} tasks remaining."


def delete_task(list_to_do, task):
    if task in list_to_do:
        list_to_do.remove(task)
        N = len(list_to_do)
        return f"Task successfully deleted. {N} tasks remaining."
    else:
        return f"Task '{task}' not found."


def move_task(task, from_index, to_index):
    list_to_do = list.pop(from_index)       
    list_to_do.insert(task, to_index)       
    return f"Task '{task}' successfully moved to index {to_index}."
    





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
