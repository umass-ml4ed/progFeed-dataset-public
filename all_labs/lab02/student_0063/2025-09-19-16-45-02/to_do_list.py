# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED


# This is a starting example. You do NOT need to modify this function
def clear_tasks(list):
  list.clear()

# Create an empty list
to_do_list = []


# Below please implement the add_task, delete_task, and move_task functions
# ----- YOUR CODE STARTS HERE -----

'''implement a function called add_task. This function should take two parameters: 
a list object representing the to-do list, 
and a string object representing (the description of) a task. Your function should  
Add that task to the end of the list.

Return an acknowledgement, which should be a string formatted exactly as: 
Task successfully added. N tasks remaining.

where N is the total number of tasks currently in the to-do list. Your returned string must match the format above exactly -- pay attention to the space characters. Do not include any extra white space characters.'''


def add_task(to_do_list, task):
    to_do_list.append(str(task))
    N = len(to_do_list)
    return 'Task successfully added. ' + str(N) + ' tasks remaining.'
print(add_task(to_do_list, 'zybook reading'))


''' implement a function called delete_task. 
This function should take two parameters: 
a list object representing the to-do list, 
and a string object representing (the description of) a task to be deleted. Your function should: Delete that task from the list. 
You can assume that the task exists in the to-do list, and also that there are no duplicates in the to-do list.
Return an acknowledgement, which should be a string formatted exactly as: 
Task successfully deleted. N tasks remaining.
where N is the number of tasks in the to-do list after the removal. 
'''

def delete_task(to_do_list, task):
   to_do_list.remove(str(task))
   N = len(to_do_list)
   return 'Task successfully deleted. ' + str(N) + ' tasks remaining.'
print(delete_task(to_do_list, 'zybook reading'))

'''implement a function called move_task. This function should take three parameters -- 
a list object representing the to-do list, 
the index of a to-do item that you want to move (we can call this the from_index), 
and an index where you want it to be moved to (call this the to_index).
Your function should:
Move the to-do list item currently at the from_index to the to_index, and ordering of all other items should remain the same as before. 
You can assume both from_index and to_index are valid, so there will NOT be an out of range error.
Return an acknowledgement, which should be a string formatted exactly as: 
Task 'T' successfully moved to index J
where T is the description of the task surrounded by single quotes ' and J is the index it has been moved to. 
Note there is no dot at the end of the printout.
'''




def move_task(to_do_list, from_index, to_index):
    task = to_do_list.pop(from_index)
    to_do_list.insert(to_index, task)
    return "Task " + "'" + str(to_do_list[to_index]) + "'" +  " successfully moved to index " + str(to_index)


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
