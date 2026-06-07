#Author   : REDACTED
#Email    : REDACTED
#Spire ID : REDACTED

def clear_tasks(to_do_list):
  to_do_list.clear()

to_do_list = []

def add_task(to_do_list, task):
    to_do_list.append(task)
    N = len(to_do_list)
    return f"Task successfully added. {N} tasks remaining."

to_do_list = []

def delete_task(to_do_list, task):
   to_do_list.remove(task)
   N = len(to_do_list)
   return f"Task successfully deleted. {N} tasks remaining."

to_do_list = []

def move_task(to_do_list, task):
   to_do_list.pop(task)
   to_do_list.insert(task)
   T = len(to_do_list)
   J = len(to_do_list)
   return f"Task {T} suceessfully moved to index {J}"

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
