# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, temperature = 68):
        self.default = temperature
        self.schedule = {}
    def add_schedule(self, time, temperature):
        self.schedule[time] = temperature
    def __str__(self):
        loop = ''
        loop += f'Default temperature: {self.default} degrees\n'
        list = sorted(self.schedule)
        for i in list:
            loop += (f'{i} {self.schedule[i]} degrees\n')
        return loop.strip()
    def get_target_temperature(self, string):
        if len(self.schedule) == 0:
            return self.default
        else:
            list = sorted(self.schedule)
            if string in list:
                return self.schedule[string]
            list.append(string)
            newlist = sorted(list)
            index = newlist.index(string)
            if index == 0:
                return self.default
            return self.schedule[newlist[index-1]]
            


