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
        return (f'Default temperature: {self.default} degrees' + f'{lis}')

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