# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED




def clear_tasks(to_do_list):
    """
    Clears all tasks from the to-do list.
    """
    to_do_list.clear()
    return "All tasks cleared."


# 1
# add task 
def add_task(to_do_list, task):
    """
    Adds a new task to the to-do list.

    Parameters:
        to_do_list (list): The current to-do list.
        task (str): The task description to add.

    Returns:
        str: Acknowledgement message.
    """
    to_do_list.append(task)
    return f"Task successfully added. {len(to_do_list)} tasks remaining."


# 2
# delete task

def delete_task(to_do_list, task):
    """
    Deletes a task from the to-do list.

    Parameters:
        to_do_list (list): The current to-do list.
        task (str): The task description to remove.

    Returns:
        str: Acknowledgement message.
    """
    to_do_list.remove(task)
    return f"Task successfully deleted. {len(to_do_list)} tasks remaining."


# 3
# move task 

def move_task(to_do_list, from_index, to_index):
    task = to_do_list.pop(from_index)
    to_do_list.insert(to_index, task)
    return f"Task '{task}' successfully moved to index {to_index}"




if __name__ == "__main__":
    to_do_list = []

    print(add_task(to_do_list, 'zybook reading'))
    print(add_task(to_do_list, 'do laundry'))
    print(add_task(to_do_list, 'cics110 lab 3'))
    print(to_do_list)

    print(delete_task(to_do_list, 'do laundry'))
    print(delete_task(to_do_list, 'cics110 lab 3'))
    print(to_do_list)

    add_task(to_do_list, 'do laundry')
    add_task(to_do_list, 'cics110 lab 3')
    print(to_do_list)

    print(move_task(to_do_list, 2, 0))
    print(to_do_list)
    print(move_task(to_do_list, 1, 2))
    print(to_do_list)

    print(clear_tasks(to_do_list))
    print(to_do_list)
