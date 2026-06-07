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
        i = 0
        for time in self.schedules:
            if float(in_str) >= float(time):
                i = float(time)
                continue
            else:
                break
        return self.schedules[i]

dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)
print(dev)