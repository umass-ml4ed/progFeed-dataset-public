# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def clear_tasks(list):
  list.clear()

to_do_list = []

def add_task(rep,des):
  rep.append(des)
  return "Task successfully added. " + str(len(rep)) + " tasks remaining."

add_task(to_do_list, 'zybook reading')
add_task(to_do_list, 'do laundry')
add_task(to_do_list, 'cics110 lab 3')
add_task(to_do_list, 'math homework')
add_task(to_do_list, 'grocery shopping')
#print("Task successfully added. " + str(len(to_do_list)) + " tasks remaining.")

def delete_task(rep,des):
  rep.remove(des)
  return "Task successfully deleted. " + str(len(rep)) + " tasks remaining."

delete_task(to_do_list, 'zybook reading')
delete_task(to_do_list, 'math homework')
#print("Task successfully deleted. " + str(len(to_do_list)) + " tasks remaining.")

def move_task(rep,from_index,to_index):
  store = rep.pop(from_index)
  rep.insert(to_index, store)
  return "Task '" + str(store) + "' successfully moved to index " + str(to_index)
#when switching create a temp variable

move_task(to_do_list, 2, 0)
print('Current to-do list:', to_do_list, '\n')
move_task(to_do_list, 1, 4)
print('Current to-do list:', to_do_list, '\n')