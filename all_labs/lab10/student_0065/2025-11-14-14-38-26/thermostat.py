# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self,default_temperature = 68):
        self.default = default_temperature
        self.schedule = {}

    def add_schedule(self, time, temperature):
        self.time = time
        self.temperature = temperature
        self.schedule['time'] = temperature

    def __str__(self):
        self.increasing_time = sorted(self.schedule)
        for time in self.increasing_time:
            return f"Default temperature: {self.default} degrees '\n' {self.time} {self.temperature} degrees"