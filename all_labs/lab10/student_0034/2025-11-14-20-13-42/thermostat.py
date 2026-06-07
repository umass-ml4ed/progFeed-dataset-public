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
    
    def get_target_temperature(self, query)


dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)
print(dev)