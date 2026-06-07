# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__ (self, temp = 68):
        self.dict = {"Default Temperature" : f"{temp} degrees"}
    def add_schedule(self, time, temp):
        self.dict[time] = temp
    def __str__(self):
        self.string = f"Default temperature: {self.dict["Default Temperature"]} degrees"
        for key in self.dict.keys():
                self.string += f"{key} {self.dict[key]}"

