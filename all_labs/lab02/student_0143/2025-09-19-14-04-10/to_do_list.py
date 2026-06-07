# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def clear_tasks(list):
  list.clear()

def add_task(list, task):
    list.append(task)
    return f'Task successfully added. {len(list)} tasks remaining.'

def delete_task(list, task):
    list.remove(task)
    return f'Task successfully deleted. {len(list)} tasks remaining.'

def move_task(list, from_index, to_index):
  task = list[from_index]
  list.pop(from_index)
  list.insert(to_index, task)
  return f'Task \'{task}\' successfully moved to index {to_index}'

to_do_list = []



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
print(move_task(to_do_list, 1, 2))
print('Current to-do list:', to_do_list, '\n')

