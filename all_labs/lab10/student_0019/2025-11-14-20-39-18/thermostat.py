# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temp = 68):
        self.default_temp = default_temp
        self.schedules = {}

    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature

def __str__(self):
    result = f"Default temperature {self.default_temp}"
    for time in sorted(self.schedules):
        self.schdules[time] = self.default_temp = 68 
