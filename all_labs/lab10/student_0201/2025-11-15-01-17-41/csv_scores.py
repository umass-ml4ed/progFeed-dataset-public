# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

import csv

def read_csv(fname):
    try:
        with open(fname, 'r') as file:
            reader = csv.reader(file)
            students = []
            has_rows = False

            for row in reader:
                has_rows = True
                name = row[0]

                section = row[1]
                scores = []
                for x in row[2:]:
                    scores.append(float(x))
                avg = round(sum(scores) / len(scores), 3)
                students.append({
                    'name': name,
                    'section': section,
                    'scores': scores,
                    'average': avg
                })
            if not has_rows:
                return None
            return students
        
    except (FileNotFoundError, IsADirectoryError):
        print(f"Error occurred when opening {fname} to read")
        return None
    except Exception:
        print(f"Error occurred when opening {fname} to read")
        return None
    

def write_csv(fname, student_data):
    try:
        with open(fname, 'w') as file:
            for student in student_data:
                # Convert all scores to strings
                scores = [str(score) for score in student['scores']]
                row_items = [student['name'], student['section']] + scores
                line = ",".join(row_items)
                file.write(line + "\n")
    except Exception:
        print(f"Error occurred when opening {fname} to write")
        return


def filter_section(student_data, section_name):
    result = []
    for student in student_data:
        if student['section'] == section_name:
            result.append(student)
    return result


def filter_average(student_data, min_inc, max_exc):
    result = []
    for s in student_data:
        if min_inc <= s['average'] < max_exc:
            result.append(s)
    return result


def split_section(fname):
    data = read_csv(fname)
    if data is None:
        return
    sections = {s['section'] for s in data}
    base = fname.split(".")[0]
    for sec in sections:
        sec_data = filter_section(data, sec)
        out_file = f"{base}_section_{sec}.csv"
        write_csv(out_file, sec_data)


def get_assignment_stats(student_data):

    def get_stats(nums):
        mean = sum(nums) / len(nums)
        mn = min(nums)
        mx = max(nums)
        rng = mx - mn
        std = (sum((x - mean) ** 2 for x in nums) / len(nums)) ** 0.5
        return {'mean': mean, 'std_dev': std, 'min': mn, 'max': mx, 'range': rng}
    return_list = []
    avg_vals = [s['average'] for s in student_data]
    return_list.append(get_stats(avg_vals))

    for i in range(10):
        nums = [s['scores'][i] for s in student_data]
        return_list.append(get_stats(nums))
    return return_list