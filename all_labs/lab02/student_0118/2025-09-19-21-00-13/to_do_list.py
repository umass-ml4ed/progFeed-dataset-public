# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED


# This is a starting example. You do NOT need to modify this function
def clear_tasks(list):
  list.clear()

# Create an empty list
to_do_list = []


#add_task
def add_task(to_do_list, task):
  
   to_do_list.append(task)
   number = str(len(to_do_list))
   return("Task successfully added. " + number + " tasks remaining.")
print(add_task(to_do_list, 'zybook reading'))
print(add_task(to_do_list, 'do laundry'))

#delete_task
def delete_task(to_do_list, task):
   to_do_list.remove(task)
   number = str(len(to_do_list))
   return("Task successfully removed. " + number + " tasks remaining.")
print(delete_task(to_do_list, 'zybook reading'))


#move_task
to_do_list = ['zybook reading', 'do laundry', 'cics110 lab 3']

def move_task(to_do_list, from_index, to_index):
   task = to_do_list.pop(from_index)
   to_do_list.insert(to_index, task)
   return("Task '" + task + "' successfully moved to index " + str(to_index))
print(move_task(to_do_list, 2, 0))
print('Current to-do list:', to_do_list, '\n')



