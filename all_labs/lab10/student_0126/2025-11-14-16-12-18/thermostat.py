# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, temperature = 68):
        self.temperature = temperature
        self.schedules = {}
    
    def add_schedule(self, time, temp):
        self.schedules[time] = temp

    def __str__(self):
        what = f'Default temperature: {self.temperature} degrees'
        for i in sorted(self.schedules):
            what += f'\n{i} {self.schedules[i]} degrees'
        return what
    
    def get_target_temperature(self, time):
        for i in range(len(self.schedules)):
            if time >= sorted(self.schedules)[i] and time >= sorted(self.schedules)[i]:
                    if i == len(sorted(self.schedules)) - 1:
                        return self.schedules[sorted(self.schedules)[i]]
                    elif time < sorted(self.schedules)[i + 1] and time < sorted(self.schedules)[i + 1]:
                            return self.schedules[sorted(self.schedules)[i]]
    
# e = Thermostat(75)
# e.add_schedule('10:10', 76)
# e.add_schedule('10:10', 73)
# e.add_schedule('07:10', 90)
# e.add_schedule('08:39', 50)
# print(e)
# print(e.get_target_temperature('11:40'))