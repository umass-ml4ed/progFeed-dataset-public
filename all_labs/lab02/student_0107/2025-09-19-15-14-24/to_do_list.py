# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

# This is a starting example. You do NOT need to modify this function
def clear_tasks(list):
  list.clear()


#adds a task to the to do list 

# Create an empty list
to_do_list = []

# Below please implement the add_task, delete_task, and move_task functions
# ----- YOUR CODE STARTS HERE -----
def add_task(lst,item):
    lst.append(item)
    return (f"Task successfully added. {len(lst)} tasks remaining.")

def delete_task(lst, task):
  lst.remove(task) 
  return(f"Task successfully deleted. {len(lst)} tasks remaining.")

def move_task(lst, from_index, to_index):
  #print(lst[from_index], lst[to_index] )
  element = [lst[from_index]] # this = the element in the list at index from_index 
  #print(element)
  lst[to_index] = lst[from_index] 
  lst[from_index] = element[0]
  
  return (f"Task '{lst[from_index]}' successfully moved to index {to_index}")

    
  
#print(add_task(to_do_list, 'zybook reading'))
#Task successfully added. 1 tasks remaining.

#print(add_task(to_do_list, 'do laundry'))
#Task successfully added. 2 tasks remaining.

#print(add_task(to_do_list, 'cics110 lab 3'))
#Task successfully added. 3 tasks remaining.

#print(add_task(to_do_list,"hello"))
#print(to_do_list)

# ===== YOUR CODE ENDS HERE =====

# You can use the code below to help test your functions

# Uncomment the following 5 lines (i.e. remove the # characters on each line) to test add_task#print(add_task(to_do_list, 'zybook reading'))
#print(add_task(to_do_list, 'do laundry'))
#print(add_task(to_do_list, 'cics110 lab 3'))
#print(add_task(to_do_list, 'math homework'))
#print(add_task(to_do_list, 'grocery shopping'))
#add_task([], "Buy groceries")

 

# Uncomment the following 2 lines (i.e. remove the # characters on each line) to test delete_task
#print(delete_task(to_do_list, 'zybook reading'))
#print(delete_task(to_do_list, 'math homework'))

# Uncomment the following 5 lines (i.e. remove the # characters on each line) to test move_task
to_do_list = ['zybook reading', 'do laundry', 'cics110 lab 3', 'math homework', 'grocery shopping']
print(move_task(to_do_list, 2, 0))
print('Current to-do list:', to_do_list, '\n')
print(move_task(to_do_list, 1, 4))
print('Current to-do list:', to_do_list, '\n')