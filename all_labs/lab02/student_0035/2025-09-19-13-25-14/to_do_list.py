#Author : REDACTED
#Email : REDACTED
#SPIRE ID : REDACTED

to_do_list = ['zybook reading', 'do laundry', 'cics110 lab 3']

def add_task(to_do_list, task):
    to_do_list.append(task)
    total_tasks = len(to_do_list)
    return f"Task successfully added. {total_tasks} tasks remaining."



def delete_task(to_do_list, task):
    to_do_list.remove(task)
    total_tasks = len(to_do_list)
    return f"Task successfully deleted. {total_tasks} tasks remaining."



print(add_task(to_do_list, 'reading'))
print(add_task(to_do_list, 'walking'))
print(add_task(to_do_list, 'sleeping'))


def move_task(to_do_list, a, b):
    to_do_list[a], to_do_list[b] = to_do_list[b], to_do_list[a]
    return f"Task {to_do_list[b]} successfully moved to index {b}"

print(move_task(to_do_list, 2,0))
print(to_do_list)