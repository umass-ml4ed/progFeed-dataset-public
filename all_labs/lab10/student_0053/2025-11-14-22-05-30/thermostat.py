# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

import copy


class Thermostat:
    def __init__(self, temp = 68):
        self.temp = temp
        self.sche = {}
    
    def add_schedule(self, time, temp):
        self.sche[time] = temp

    def __str__(self):
        time_sorted = sorted(self.sche)
        s = f'Default temperature: {self.temp} degrees'
        for i in time_sorted:
            s += f'\n{i} {self.sche[i]} degrees'
        return s 
    
    def get_target_temperature(self, time):
        schedule = copy.deepcopy(self.sche)
        if '00:00' not in schedule:
            schedule['00:00'] = self.temp
        time_sorted = sorted(schedule)
        time_sorted.append('24:00')
        print(time_sorted)
        index = 1
        while index < len(time_sorted):
            print(time_sorted[index])
            for i in range(0, 5):
                print(i)
                if i != 2:
                    if int(time[i]) < int(time_sorted[index][i]):
                        return schedule[time_sorted[index - 1]]
                    elif int(time[i]) > int(time_sorted[index][i]):
                        break
            index += 1

