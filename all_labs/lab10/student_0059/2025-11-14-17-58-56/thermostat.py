# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat:
    def __init__(self, temp=68):
        self.temp = temp
        self.schedule = {}
    def add_schedule(self, time, temperature):
        self.schedule[time] = temperature
    def __str__(self):
        a = (f"Default temperature: {self.temp} degrees\n")
        x = sorted(self.schedule)
        l = len(x)
        y = 0
        for i in x:
            a += (f"{i} {self.schedule[i]} degrees")
            if y < l -1:
                a += "\n"
            y += 1
        return a
    def get_target_temperature(self, time):
        if len(self.schedule) == 0:
            return self.temp
        x = sorted(self.schedule)
        if time < x[0]:
            return self.temp
        temp_time = x[0]
        for b in x:
            if b <= time:
                temp_time = b
        return self.schedule[temp_time]
    

dev = Thermostat(75)
dev.add_schedule("08:00", 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)
print(dev)
print(dev.get_target_temperature('23:00'))
print(dev.get_target_temperature('16:35'))
print(dev.get_target_temperature('05:55'))
print(dev.get_target_temperature('08:00')) 
print(dev.get_target_temperature('12:00'))

