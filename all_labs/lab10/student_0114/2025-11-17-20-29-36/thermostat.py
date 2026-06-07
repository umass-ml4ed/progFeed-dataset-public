# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostate:
    """this class is titled thermostat"""
    def __init__ (self, temp = 68):
        self.dict = {"Default Temperature" : f"{temp} degrees"}
    def add_schedule(self, time, temp):
        self.dict[time] = temp
    def __str__(self):
        self.string = f"Default temperature: {self.dict["Default Temperature"]} degrees"
        for key in self.dict.keys():
                self.string += f"{key} {self.dict[key]}"

dev = Thermostate(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)
print(dev.dict)
