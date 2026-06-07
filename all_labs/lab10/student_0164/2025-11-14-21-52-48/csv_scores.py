import csv

# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

def read_csv(fname):
    try:
        with open(fname, 'r', newline='') as f:


            reader = csv.reader(f)
            if not reader:
                return None
            students = []

            for row in reader:
                name = row[0]
                section = row[1]
                scores = [float(x) for x in row[2:]]
                avg = round(sum(scores) / len(scores), 3)
                student_dict = {
                    'name': name,
                    'section': section,
                    'scores': scores,
                    'average': avg

                }
                students.append(student_dict)
            return students 
    except (FileNotFoundError, IsADirectoryError):
        print(f"Error occurred when opening {fname} to read")
        return None








def write_csv(fname, student_data):
    try:
        with open(fname, 'w') as f:
            for student in student_data:
                row_items = [student['name'], student['section']] + [str(score) for score in student['scores']]
                row = ",".join(row_items)
                f.write(row + "\n")
    except Exception:
        print(f"Error occurred when opening {fname} to write")
        return 


            


import os
def filter_section(student_data, section_name):
    return [student for student in student_data if student['section'] == section_name]

def filter_average(student_data, min_inc, max_exc):
    return [student for student in student_data if min_inc <= student['average'] < max_exc]

def split_section(fname):
    student_data = read_csv(fname)
    if student_data is None:
        return
    sections = {student['section'] for student in student_data}
    base_name = os.path.splitext(fname)[0]
    for section in sections:
        section_data = [student for student in student_data if student['section'] == section]
        out_fname = f"{base_name}_section_{section}.csv"
        write_csv(out_fname, section_data)



def get_stats(nums):
    mean = sum(nums) / len(nums)
    minimum = min(nums)
    maximum = max(nums)
    range_val = maximum - minimum
    std_dev = (sum((n-mean) ** 2 for n in nums) /len(nums)) ** 0.5
    return  {
        'mean': mean,
        'std_dev': std_dev,
        'min': minimum,
        'max': maximum,
        'range': range_val
    }

def get_assignment_stats(student_data):
    return_list = []
    averages = [student['average'] for student in student_data]
    return_list.append(get_stats(averages))
    for i in range(10):
        scores_i = [student['scores'][i] for student in student_data]
        return_list.append(get_stats(scores_i))
    return return_list
