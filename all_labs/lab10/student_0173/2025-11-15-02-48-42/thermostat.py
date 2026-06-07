# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat:
    def __init__(self, temp = 68):
        self.temp = temp
        self.schedule = {}
    def add_schedule(self, time, temp):
        self.schedule[time] = temp
    def __str__(self):
        sorted_list = sorted(self.schedule)
        message = ''
        for i in sorted_list:
            message += f'\n{i} {self.schedule[i]} degrees'
        return(f"Default temperature: {self.temp} degrees {message}")
    def get_target_temperature(self, time):
        sorted_list = sorted(self.schedule)
        min_time = self.temp
        for i in sorted_list:
            if time >= i:
                min_time = self.schedule[i]
            else:
                continue
        return min_time
        
#dev = Thermostat(75)
#dev.add_schedule('08:00', 60.4)
#dev.add_schedule('19:35', 75.5)
#dev.add_schedule('09:30', 58.2)
#dev.add_schedule('22:39', 68.2)
#print(dev)
#print(dev.get_target_temperature('23:00')) 
#print(dev.get_target_temperature('16:35'))
#print(dev.get_target_temperature('05:55'))
#print(dev.get_target_temperature('08:00'))
#print(dev.get_target_temperature('12:00'))