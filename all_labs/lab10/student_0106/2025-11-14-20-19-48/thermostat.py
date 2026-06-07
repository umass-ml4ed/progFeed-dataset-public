# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, inittemp = 68):
        self.temp = inittemp
        self.schedule = {} 

    def add_schedule(self, time, temp):
        self.schedule[time] = temp
    
    def __str__(self):
        string = f"Default temperature: {self.temp} degrees"
        for time in self.schedule:
            string += f"\n{time} {self.schedule[time]} degrees"
        return string
    
    def get_target_temperature(self, timeinput):
        returntemp = self.temp
        targettime = 0

        for time in self.schedule:
            if int(time[0:2] + time[3:5]) <= int(timeinput[0:2] + timeinput[3:5]) and int(time[0:2] + time[3:5]) > targettime:
                targettime = int(time[0:2] + time[3:5])
                returntemp = self.schedule[time]
        
        return returntemp
            




dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)
print(dev)

dev.get_target_temperature('23:00') 
dev.get_target_temperature('16:35') 
dev.get_target_temperature('05:55') 
dev.get_target_temperature('08:00') 
dev.get_target_temperature('12:00')
