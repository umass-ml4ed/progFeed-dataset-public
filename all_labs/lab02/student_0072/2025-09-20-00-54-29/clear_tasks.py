# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def clear_task(to_do: list) -> None: # task remove
    to_do.clear

def add_task(to_do: list, task: str) -> str: # task add
    to_do.append(task) #leftover task count
    n = len(to_do)
    return "Task successfully added. " + str(n) + " tasks remaining."

# same thing but for remove
def delete_task(to_do: list, task: str) -> str: 
    to_do.remove(task)
    n = len(to_do)
    return "Task successfully deleted. " + str(n) + " tasks remaining."

# same thing but for rank (index) of task
def move_task(to_do: list, from_index: int, to_index: int) -> str: # take out task
    task = to_do.pop(from_index) 
    to_do.insert(to_index, task) 
    return "Task '" + task + "' successfully moved to index " + str(to_index)
