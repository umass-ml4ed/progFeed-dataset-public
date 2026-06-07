# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, temp:float = 68):
        self.default = temp
        self.schedule = {}

    def add_schedule(self,time:str,temp:float):
        self.schedule[time] = temp

    def __str__(self):
        sort = sorted(self.schedule.keys(), key=lambda time: [int(x) for x in time.split(":")])
        lis = '\n'.join([f'{time} {self.schedule[time]} degrees' for time in sort])
        return (f'Default temperature: {self.default} degrees'
                f'{lis}')

    def get_target_temperature(self,time:str):
        if time in self.schedule:
            return self.schedule[time]
        else:
            temp = list(self.schedule.keys())
            temp.append(time)
            sort = sorted(temp, key=lambda time: [int(x) for x in time.split(":")])
            if sort.index(time) != 0:
                return self.schedule[sort[sort.index(time)-1]]
            else:
                return self.default

dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)
print(dev)
assert 68.2 == dev.get_target_temperature('23:00')
assert 58.2 == dev.get_target_temperature('16:35')
assert 75 == dev.get_target_temperature('05:55')
assert 60.4 == dev.get_target_temperature('08:00')
assert 58.2 == dev.get_target_temperature('12:00')



