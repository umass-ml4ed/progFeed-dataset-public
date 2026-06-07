#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED


# This is a starting example. You do NOT need to modify this function
def clear_tasks(list):
  list.clear()

# Create an empty list
to_do_list = []

def add_task(to_do_list, b):
  bc = (to_do_list.append(b))
  cd = len(to_do_list)
  if to_do_list[-1]==b:
    return ("Task succesfully added." + str(cd) +"tasks remaining." )

