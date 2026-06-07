# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def clear_tasks(list):
  list.clear()

to_do_list = []

def add_task(rep,des):
  addFunc = rep.append(des)
  return addFunc
#print("Task successfully added. " + str(len(to_do_list)) + " tasks remaining.")

print(add_task(to_do_list, 'zybook reading'))
print(add_task(to_do_list, 'do laundry'))
print(add_task(to_do_list, 'cics110 lab 3'))
print(add_task(to_do_list, 'math homework'))
print(add_task(to_do_list, 'grocery shopping'))

print("Task successfully added. " + str(len(to_do_list)) + " tasks remaining.")
print(to_do_list)

# Uncomment the following 2 lines (i.e. remove the # characters on each line) to test delete_task
#print(delete_task(to_do_list, 'zybook reading'))
#print(delete_task(to_do_list, 'math homework'))

# Uncomment the following 5 lines (i.e. remove the # characters on each line) to test move_task
#to_do_list = ['zybook reading', 'do laundry', 'cics110 lab 3', 'math homework', 'grocery shopping']
#print(move_task(to_do_list, 2, 0))
#print('Current to-do list:', to_do_list, '\n')
#print(move_task(to_do_list, 1, 4))
#print('Current to-do list:', to_do_list, '\n')