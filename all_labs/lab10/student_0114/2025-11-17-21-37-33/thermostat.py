# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__ (self, temp = 68):
        self.default_temp = temp
        self.schedules = {}
    def add_schedule(self, time, temp):
        self.schedules[time] = temp
    def __str__(self):
        lst = sorted(self.schedules)
        self.string = f"Default temperature: {self.default_temp} degrees\n"
        count = 0
        while count < len(lst):
                self.string += f"{lst[count]} {self.schedules[lst[count]]} degrees"
                if count != (len(lst)-1):
                     self.string += "\n"
                count += 1
        return self.string

dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)

print(dev.schedules)
str(dev)
print(dev.string)