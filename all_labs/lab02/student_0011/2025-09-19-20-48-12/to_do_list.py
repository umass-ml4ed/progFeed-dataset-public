#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED


# This is a starting example. You do NOT need to modify this function
def clear_tasks(list):
  list.clear()

# Create an empty list
to_do_list = []

def add_task(to_do_list, b):
  to_do_list.append(b)
  cd = len(to_do_list)
  return "Task successfully added. " + str(cd) +" tasks remaining."
#Task successfully added. N tasks remaining.
print(add_task(to_do_list, "hw"))

def delete_task(to_do_list, x):
  to_do_list.remove(x)
  bc = len(to_do_list)
  return "Task successfully deleted. " + str(bc) + " tasks remaining."

def move_task(to_do_list, from_index, to_index):
  task = to_do_list.pop(from_index)
  to_do_list.insert(to_index, task)
  return "task " + str(task) + " successfully moved to index " + str(to_index)

  

