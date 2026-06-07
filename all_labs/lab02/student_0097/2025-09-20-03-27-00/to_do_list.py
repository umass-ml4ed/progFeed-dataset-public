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


def add_task(x,y):
 to_do_list.append(y)
 n = len(to_do_list)
 z = "Task successfully added.",n,"tasks remaining."
 return z
print(add_task(to_do_list,'zybook reading'))
print(add_task(to_do_list,'complete code'))
print(add_task(to_do_list,'turn in code'))



def delete_task(x,y):
 to_do_list.remove(y)
 n = len(to_do_list)
 z = "Task successfully removed.",n,"tasks remaining."
 return z
print(delete_task(to_do_list,'zybook reading'))
print(add_task(to_do_list,'zybook reading'))


def move_task(x,y):
 to_do_list.pop(y)
T = 
 z = "Task",n,"successfully moved to index 0"
print(to_do_list)
print(move_task(to_do_list, 2, 0))
print(to_do_list)


#x = to_do_list
# y = input("Type Something: ")


#This is what we want to return:
#Task successfully added. 1 task remaining.

#y = input("Enter a task: ")
#to_do_list.append(y)
#n = len(to_do_list)
#print(add_task(to_do_list,y))
#print("Task successfully added.",n,"tasks remaining")


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
