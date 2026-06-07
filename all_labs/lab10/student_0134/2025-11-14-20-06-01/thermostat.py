# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self,default=68):
        self.d_temp=default
        self.schedules={}
    def add_schedule(self,time:str,temp:float):
        self.schedules[time]=temp
    def __str__(self):
        string=f'Default temperature: {self.d_temp} degrees'
        for i in sorted(self.schedules):
            string+=f'\n{i} {self.schedules[i]} degrees'
        return string
    def get_target_temperature(self,time):
        for i in sorted(self.schedules)[::-1]:
            if i<=time:
                return self.schedules[i]
        return self.d_temp


dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)

# print(dev)

# print(dev.get_target_temperature('23:00'))
# print(dev.get_target_temperature('16:35') )
# print(dev.get_target_temperature('05:55') )
# print(dev.get_target_temperature('08:00') )
# print(dev.get_target_temperature('12:00'))

