# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:

    def __init__(self, temp=68):
        self.dtemp = temp
        self.schedules = {}

    def add_schedule(self, time, temp):
        self.schedules[time] = temp

    def __str__(self):
        lst = []
        my_thermostat = sorted(self.schedules)
        for t in my_thermostat:
            lst.append(f'{t} {self.schedules[t]} degrees')
        my_str = '\n'.join(lst)
        new_str = '\n'
        str2 = new_str + my_str if len(my_str) != 0 else my_str
        return f'Default temperature: {self.dtemp} degrees{str2}'
    
    def get_target_temperature(self, in_str):
        j = self.dtemp
        new_lst = sorted(self.schedules)
        for time in new_lst:
            if float(in_str[0], in_str[1], '.', in_str[3], in_str[4]) >= float(time[0], time[1], '.', time[3], time[4]):
                j = float(time[0], time[1], '.', time[3], time[4])
                continue
            else:
                break
        return self.schedules[j] if j != self.dtemp else j

dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)
print(dev)