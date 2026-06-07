# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

# This is a starting example. You do NOT need to modify this function
def clear_tasks(list):
  list.clear()

# Create an empty list
to_do_list=[]

# Below please implement the add_task, delete_task, and move_task functions
# ----- YOUR CODE STARTS HERE -----
def add_task(list,a):
  to_do_list.append(a)
  return("Task successfully added. "+str(len(to_do_list)))+" Tasks remaining."

def delete_task(list,a):
  to_do_list.remove(a)
  return("Task successfully deleted. "+str(len(to_do_list))+ " Tasks remaning.")

def move_task(list,a, b):
  from_index=to_do_list[a]
  to_do_list.pop(a)
  to_do_list.insert(b, from_index)
  return("Task "+str(from_index)+" successfully moved to index "+str(b))
# ===== YOUR CODE ENDS HERE =====