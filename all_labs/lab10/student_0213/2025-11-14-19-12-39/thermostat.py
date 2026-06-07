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
        return f'Default temperature: {self.dtemp} degrees{my_str}'

dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)
print(dev)