# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

import csv

def read_csv(fname):

    try:

        std = []
        
        with open(fname, 'r') as file:

            for c in file.readlines():

                std.append(c.strip().split(','))

            if not fname:

                return None

            if not std:

                return None

            final = []

            for student in std:

                scores = [float(c) for c in student[2:]]

                average = sum(scores) / len(scores)

                final.append({

                    'name': student[0],

                    'section': student[1],

                    'scores': scores,

                    'average': round(average, 3)
                })

            return final
        

    except IsADirectoryError:

        print(f"Error occurred when opening {fname} to read")

        return None

    except:

        print(f"Error occurred when opening {fname} to read")

        return None
    

        

    # text = file.readlines()

    # if len(text) == 0:

    #     return None
    
    # try:

    #     for line in text:

    #         info = {}

    #         line =  line.strip().split(",")

    #         total = 0

    #         info['name'] = line[0]

    #         info['section'] = line[1]

    #         info['scores'] = line[2:] 

    #         for num in line[2:]:

    #             total += float(num)

    #         info['average'] = round(total/len(line[2:]), 3)

    #         std.append(info)

    #     file.close()

    #     return std

    # except:

    #     print(f"Error occurred when opening {fname} to read")

    #     file.close()

    #     return None




def write_csv(fname, student_data: list):

    try:

        with open(fname, 'w', newline='') as file:

            writer = csv.writer(file)

            for student in student_data:

                writer.writerow([student['name'], student['section']] + student['scores'])

    except:

        print(f"Error occurred when opening {fname} to write")

        return None




    # lest = []

    # try:

    #     file = open(f"{fname}", "w", newline = '')

    # except:

    #     print(f'Error occurred when opening {fname} to write')

    #     return None

    # try:

    #     for i in range(len(student_data)):

    #         ls = []

    #         del student_data[i]['average']

    #         for key in student_data[i]:

    #             ls.append(student_data[i][key])

    #         flat = []
            
    #         for item in ls[-1]:

    #             flat.append(item)

    #         ls.pop(-1)

    #         for item in flat:

    #             ls.append(item)

    #         text = ",".join(ls)

    #         lest.append(text)

    #     for i in range(len(lest)):

    #         if i != len(lest) -1:

    #             file.write(lest[i] +"\n")
    #         else:

    #             file.write(lest[i])

    #     file.close()

    # except:

    #     file.close()

    #     return None






def filter_section(student_data: list, section_name: str) -> list:
    try:

        lee = [student for student in student_data if student['section'] == section_name]

        '''for student in student_data:

            if student['section'] ==  section_name:

                lee.append(student)'''

        return lee

    except:

        return None



def filter_average(student_data: list, min_inc: float, max_exc: float) -> list:

    try:

        leee = [student for student in student_data if (student['average'] < max_exc) and (student['average'] >= min_inc)]

        '''for student in student_data:

            if student['average'] < max_exc and student['average'] >= min_inc:

                lee.append(student)'''

        return leee

    except:

        return None



def split_section(fname):

    name = fname.split(".")[0]

    try:

        le = read_csv(fname)

        se = set()

        for student in le:

            se.add(student['section'])

        for sec in se:

            lili = [student for student in le if student['section'] == sec]

            '''for student in le:

                if student['section'] == sec:

                    lili.append(student)'''

            write_csv(f"{name}_section_{sec}.csv", lili)

    except:

        return None

   
def get_assignment_stats(student_data: list) -> list:

    try:
        data = {}

        return_list = []

        numbs = [student['average'] for student in student_data]

        def get_stats(nums: list):

            mean = sum(nums) / len(nums)

            minimum = min(nums)

            maximum = max(nums)

            range_ = maximum - minimum

            std_dev = (sum([(n - mean)**2 for n in nums]) / len(nums)) ** (1/2)

            return mean, round(minimum, 3), round(maximum, 3), round(range_, 3), std_dev

        data["mean"] = get_stats(numbs)[0]
        
        data["std_dev"] = get_stats(numbs)[4]

        data["min"] = get_stats(numbs)[1]

        data["max"] = get_stats(numbs)[2]

        data["range"] = get_stats(numbs)[3]

        return_list.append(data)

        for i in range(10):

            score = [student['scores'][i] for student in student_data]

            dictio = {}

            dictio["mean"] = get_stats(score)[0]

            dictio["std_dev"] = get_stats(score)[4]

            dictio["min"] = get_stats(score)[1]

            dictio["max"] = get_stats(score)[2]

            dictio["range"] = get_stats(score)[3]

            return_list.append(dictio)




        return return_list

    except Exception as e:

        return e


        



            












