# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat:
    def __init__(self, temp=68, schedule={}):
        self.temp = temp
        self.schedule = schedule

    def add_schedule(self, time, temp):
        self.schedule[time] = temp 
        return self.schedule
    
    def __str__(self):
        ans = f"Default Temperature: {self.temp}\n"
        l = sorted(self.schedule)
        for i in range(len(l)):
            ans = ans + f"{l[i]} {self.schedule[l[i]]} degrees" + "\n"
        return ans



dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)
print(Thermostat())
