# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat:
    def __init__(self, temp=68):
        self.temp = temp
        self.schedule = {}

    def add_schedule(self, time, temp):
        self.schedule[time] = temp 
        return self.schedule
    
    def __str__(self):
        ans = f"Default temperature: {self.temp} degrees"
        l = sorted(self.schedule)
        for i in range(len(l)):
            ans = ans + f"\n{l[i]} {self.schedule[l[i]]} degrees"  
        return ans

    def get_target_temperature(self, time):
        l = sorted(self.schedule)
        t = l[0]
        if time < l[0]:
            return self.temp
        for i in l:
            if int(i.replace(":", "")) <= int(time.replace(":","")):
                t = i

        return self.schedule[t]

 
dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)
dev.get_target_temperature('23:00') 
dev.get_target_temperature('16:35') 
dev.get_target_temperature('05:55') 
dev.get_target_temperature('08:00') 
dev.get_target_temperature('12:00') 
print(dev)