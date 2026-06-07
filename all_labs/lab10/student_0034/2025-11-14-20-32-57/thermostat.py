# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:

    def __init__(self, temp=68):
        self.temp = temp
        self.sched = {}
    
    def add_schedule(self, time, temperature):
        self.sched[time] = temperature
    
    def __str__(self):
        timelist = sorted(self.sched)
        result = f"Default temperature: {self.temp} degrees"
        for time in timelist:
            result += f"\n{time} {self.sched[time]} degrees"
        return result
    
    def get_target_temperature(self, query):
        timelist = sorted(self.sched)
        temp = self.temp
        for time in timelist:
            if time <= query:
                temp = self.sched[time]
            else:
                break
        return temp


dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('22:39', 68.2)
print(dev.get_target_temperature('23:00')) 
print(dev.get_target_temperature('16:35')) 
print(dev.get_target_temperature('05:55')) 
print(dev.get_target_temperature('08:00')) 
print(dev.get_target_temperature('12:00'))

